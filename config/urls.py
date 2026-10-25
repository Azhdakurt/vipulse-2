from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LoginView
from players.forms import BootstrapAuthenticationForm

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "accounts/login/",
        LoginView.as_view(
            template_name="registration/login.html",
            authentication_form=BootstrapAuthenticationForm,
        ),
        name="login",
    ),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("players.urls")),
]
