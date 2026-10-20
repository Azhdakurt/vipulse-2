from django.contrib import admin
from .models import Player, Review


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        "player_id",
        "username",
        "vip_tier",
        "created_at"
    )
    search_fields = ("player_id", "username")
    list_filter = ("vip_tier",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "player",
        "risk_level",
        "retention_score",
        "created_at"
    )
    search_fields = (
        "player__username",
        "player__player_id"
    )
    list_filter = ("risk_level",)
