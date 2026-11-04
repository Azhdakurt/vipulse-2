from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Player, Review


class AuthenticationTests(TestCase):

    def test_player_list_requires_login(self):
        response = self.client.get(reverse("player_list"))

        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response.url)

    def test_logged_in_user_can_access_player_list(self):
        User = get_user_model()
        User.objects.create_user(
            username="testuser",
            password="TestPassword123!"
        )

        self.client.login(
            username="testuser",
            password="TestPassword123!"
        )

        response = self.client.get(reverse("player_list"))

        self.assertEqual(response.status_code, 200)


class PlayerCRUDTests(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123!"
        )
        self.client.force_login(self.user)

    def test_player_creation(self):
        response = self.client.post(
            reverse("player_create"),
            {
                "player_id": "VIP1001",
                "username": "TestPlayer",
                "vip_tier": "gold",
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Player.objects.count(), 1)

        player = Player.objects.get(player_id="VIP1001")

        self.assertEqual(player.username, "TestPlayer")
        self.assertEqual(player.vip_tier, "gold")

    def test_player_update(self):
        player = Player.objects.create(
            player_id="VIP1002",
            username="OriginalPlayer",
            vip_tier="bronze"
        )

        response = self.client.post(
            reverse("player_update", args=[player.pk]),
            {
                "player_id": "VIP1002",
                "username": "UpdatedPlayer",
                "vip_tier": "diamond",
            }
        )

        self.assertEqual(response.status_code, 302)

        player.refresh_from_db()

        self.assertEqual(player.username, "UpdatedPlayer")
        self.assertEqual(player.vip_tier, "diamond")
        self.assertEqual(Player.objects.count(), 1)

    def test_player_delete(self):
        player = Player.objects.create(
            player_id="VIP1003",
            username="DeleteTestPlayer",
            vip_tier="silver"
        )

        response = self.client.post(
            reverse("player_delete", args=[player.pk])
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Player.objects.filter(pk=player.pk).exists()
        )
        self.assertEqual(Player.objects.count(), 0)


class ReviewCRUDTests(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123!"
        )
        self.client.force_login(self.user)

        self.player = Player.objects.create(
            player_id="VIP2001",
            username="ReviewTestPlayer",
            vip_tier="gold"
        )

    def test_review_creation(self):
        response = self.client.post(
            reverse("review_create"),
            {
                "player": self.player.pk,
                "risk_level": "medium",
                "retention_score": 75,
                "notes": "Test review notes",
                "recommended_action": "Follow up with player",
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Review.objects.count(), 1)

        review = Review.objects.get()

        self.assertEqual(review.player, self.player)
        self.assertEqual(review.risk_level, "medium")
        self.assertEqual(review.retention_score, 75)
        self.assertEqual(
            review.recommended_action,
            "Follow up with player"
        )

    def test_review_update(self):
        review = Review.objects.create(
            player=self.player,
            risk_level="low",
            retention_score=40,
            notes="Original notes",
            recommended_action="Original action"
        )

        response = self.client.post(
            reverse("review_update", args=[review.pk]),
            {
                "player": self.player.pk,
                "risk_level": "high",
                "retention_score": 85,
                "notes": "Updated notes",
                "recommended_action": "Updated action",
            }
        )

        self.assertEqual(response.status_code, 302)

        review.refresh_from_db()

        self.assertEqual(review.risk_level, "high")
        self.assertEqual(review.retention_score, 85)
        self.assertEqual(review.notes, "Updated notes")
        self.assertEqual(
            review.recommended_action,
            "Updated action"
        )
        self.assertEqual(Review.objects.count(), 1)

    def test_review_delete(self):
        review = Review.objects.create(
            player=self.player,
            risk_level="medium",
            retention_score=60,
            notes="Review to delete",
            recommended_action="No action required"
        )

        response = self.client.post(
            reverse("review_delete", args=[review.pk])
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Review.objects.filter(pk=review.pk).exists()
        )
        self.assertEqual(Review.objects.count(), 0)

    def test_player_search(self):
        Player.objects.create(
            player_id="VIP3001",
            username="SearchTarget",
            vip_tier="gold"
        )

        Player.objects.create(
            player_id="VIP3002",
            username="AnotherPlayer",
            vip_tier="silver"
        )

        response = self.client.get(
            reverse("player_list"),
            {"q": "SearchTarget"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "SearchTarget")
        self.assertNotContains(response, "AnotherPlayer")

    def test_review_filtering(self):
        Review.objects.create(
            player=self.player,
            risk_level="high",
            retention_score=85,
            notes="High risk test review",
            recommended_action="High risk action"
        )

        Review.objects.create(
            player=self.player,
            risk_level="low",
            retention_score=30,
            notes="Low risk test review",
            recommended_action="Low risk action"
        )

        response = self.client.get(
            reverse("review_list"),
            {"risk_level": "high"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "High risk test review")
        self.assertNotContains(response, "Low risk test review")

    def test_dashboard_statistics(self):
        Review.objects.create(
            player=self.player,
            risk_level="high",
            retention_score=80,
            notes="High risk review",
            recommended_action="Follow up"
        )

        Review.objects.create(
            player=self.player,
            risk_level="low",
            retention_score=60,
            notes="Low risk review",
            recommended_action="Monitor"
        )

        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["total_players"], 1)
        self.assertEqual(response.context["total_reviews"], 2)
        self.assertEqual(response.context["high_risk_players"], 1)
        self.assertEqual(
            response.context["average_retention_score"], 70
        )
