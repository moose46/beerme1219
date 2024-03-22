from django import forms
from django.db.models.lookups import GreaterThan
from django.forms import DateInput
from traitlets import default

from .models import Driver, Player, Race

# Create forms here
# env > mysite > main > views.py


# https://openclassrooms.com/en/courses/7107341-intermediate-django/7264795-include-multiple-forms-on-a-page
class RaceForm(forms.ModelForm):
    edit_race = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    race_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Race
        fields = ["race_date", "track", "race_name"]


# https://openclassrooms.com/en/courses/7107341-intermediate-django/7264795-include-multiple-forms-on-a-page
class RaceDeleteForm(forms.Form):
    delete_race = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    # race_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    # race_name = forms.CharField(max_length=64, required=True, help_text="empty")
    # delete_race = forms.CheckboxInput()

    # class Meta:
    #     model = Race
    #     # fields = ["race_name", "track"]


# https://www.techwithtim.net/tutorials/django/html-templates
# https://www.techwithtim.net/tutorials/django/simple-forms
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
