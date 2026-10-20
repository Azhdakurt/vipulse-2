from django.urls import path
from . import views

urlpatterns = [
    path("", views.player_list, name="player_list"),
    path("add/", views.player_create, name="player_create"),
    path(
        "edit/<int:pk>/",
        views.player_update,
        name="player_update"
    ),
    path(
        "delete/<int:pk>/",
        views.player_delete,
        name="player_delete"
    ),
    path(
        "reviews/",
        views.review_list,
        name="review_list"
    ),
    path(
        "reviews/add/",
        views.review_create,
        name="review_create"
    ),
    path(
        "reviews/edit/<int:pk>/",
        views.review_update,
        name="review_update"
    ),
    path(
        "reviews/delete/<int:pk>/",
        views.review_delete,
        name="review_delete"
    ),
]