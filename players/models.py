from django.db import models


class Player(models.Model):
    VIP_TIERS = [
        ("bronze", "Bronze"),
        ("silver", "Silver"),
        ("gold", "Gold"),
        ("platinum", "Platinum"),
        ("diamond", "Diamond"),
    ]

    player_id = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=100)
    vip_tier = models.CharField(
        max_length=20,
        choices=VIP_TIERS,
        default="bronze"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} ({self.player_id})"
class Review(models.Model):
    RISK_LEVELS = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]

    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    risk_level = models.CharField(
        max_length=20,
        choices=RISK_LEVELS,
        default="low"
    )
    retention_score = models.PositiveIntegerField(
        default=50
    )
    notes = models.TextField()
    recommended_action = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.player.username}"
