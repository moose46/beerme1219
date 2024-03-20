from django import forms
from django.db.models.lookups import GreaterThan
from django.forms import DateInput

from .models import Driver, Player, Race

# Create forms here
# env > mysite > main > views.py


# https://www.techwithtim.net/tutorials/django/html-templates
class RaceIndexForm(forms.ModelForm):
    race_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    race_name = forms.CharField(max_length=64, required=True, help_text="empty")

    class Meta:
        model = Race
        fields = ["race_name", "track"]


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
