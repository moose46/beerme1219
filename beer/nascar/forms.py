from django import forms
from django.db.models.lookups import GreaterThan

from .models import Driver, Player, Race

# Create forms here
# env > mysite > main > views.py


class RaceForm(forms.Form):
    class Meta:
        model = Race
        fields = ["race_name", "race_date", "track"]


# https://docs.djangoproject.com/en/5.0/ref/models/expressions/
# http://127.0.0.1:8081/nascar/bets/
class BetForm(forms.Form):
    # only display race_date > 2024
    race_choice = forms.ModelChoiceField(
        queryset=Race.objects.filter(race_date__gt=("2024-01-01")).order_by(
            "race_date"
        ),
        initial=0,
        required=True,
    )
    greg_driver_choice = forms.ModelChoiceField(
        queryset=Driver.objects.all().order_by("name"), initial=0
    )
    bob_driver_choice = forms.ModelChoiceField(
        queryset=Driver.objects.all().order_by("name"), initial=0
    )
