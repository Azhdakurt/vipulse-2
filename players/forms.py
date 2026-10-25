from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Player, Review


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ["player_id", "username", "vip_tier"]

        widgets = {
            "player_id": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "username": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "vip_tier": forms.Select(
                attrs={"class": "form-select"}
            ),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "player",
            "risk_level",
            "retention_score",
            "notes",
            "recommended_action",
        ]

        widgets = {
            "player": forms.Select(
                attrs={"class": "form-select"}
            ),
            "risk_level": forms.Select(
                attrs={"class": "form-select"}
            ),
            "retention_score": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 0,
                    "max": 100,
                }
            ),
            "notes": forms.Textarea(
                attrs={"class": "form-control", "rows": 4}
            ),
            "recommended_action": forms.Textarea(
                attrs={"class": "form-control", "rows": 4}
            ),
        }

    def clean_retention_score(self):
        score = self.cleaned_data["retention_score"]

        if score < 0 or score > 100:
            raise forms.ValidationError(
                "Retention score must be between 0 and 100."
            )
        return score


class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your username",
                "autofocus": True,
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your password",
            }
        )
    )
