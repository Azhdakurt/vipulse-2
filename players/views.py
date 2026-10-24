from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Avg, Q

from .models import Player, Review
from .forms import PlayerForm, ReviewForm


@login_required
def player_list(request):
    query = request.GET.get("q", "").strip()

    players = Player.objects.all().order_by("-created_at")

    if query:
        players = players.filter(
            Q(username__icontains=query) |
            Q(player_id__icontains=query)
        )

    return render(
        request,
        "players/player_list.html",
        {
            "players": players,
            "query": query,
        }
    )


@login_required
def player_create(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Player added successfully!"
            )
            return redirect("player_list")
    else:
        form = PlayerForm()

    return render(
        request,
        "players/player_form.html",
        {"form": form}
    )


@login_required
def player_update(request, pk):
    player = get_object_or_404(Player, pk=pk)

    if request.method == "POST":
        form = PlayerForm(request.POST, instance=player)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Player updated successfully!"
            )
            return redirect("player_list")
    else:
        form = PlayerForm(instance=player)

    return render(
        request,
        "players/player_form.html",
        {"form": form}
    )


@login_required
def player_delete(request, pk):
    player = get_object_or_404(Player, pk=pk)

    if request.method == "POST":
        player.delete()
        messages.success(
            request,
            "Player deleted successfully!"
        )
        return redirect("player_list")

    return render(
        request,
        "players/player_confirm_delete.html",
        {"player": player}
    )


@login_required
def review_list(request):
    reviews = Review.objects.select_related(
        "player"
    ).order_by("-created_at")

    return render(
        request,
        "players/review_list.html",
        {"reviews": reviews}
    )


@login_required
def review_create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "VIP Review added successfully!"
            )
            return redirect("review_list")
    else:
        form = ReviewForm()

    return render(
        request,
        "players/review_form.html",
        {"form": form}
    )


@login_required
def review_update(request, pk):
    review = get_object_or_404(Review, pk=pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "VIP Review updated successfully!"
            )
            return redirect("review_list")
    else:
        form = ReviewForm(instance=review)

    return render(
        request,
        "players/review_form.html",
        {"form": form}
    )


@login_required
def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)

    if request.method == "POST":
        review.delete()
        messages.success(
            request,
            "VIP Review deleted successfully!"
        )
        return redirect("review_list")

    return render(
        request,
        "players/review_confirm_delete.html",
        {"review": review}
    )


@login_required
def dashboard(request):
    total_players = Player.objects.count()
    total_reviews = Review.objects.count()
    high_risk_players = (
     Review.objects.filter(risk_level="high")
     .values("player")
     .distinct()
     .count()
    )
    average_retention_score = Review.objects.aggregate(
        Avg("retention_score")
    )["retention_score__avg"] or 0
    context = {
        "total_players": total_players,
        "total_reviews": total_reviews,
        "high_risk_players": high_risk_players,
        "average_retention_score": average_retention_score,
    }

    return render(request, "players/dashboard.html", context)
