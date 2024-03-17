# from django import template

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from .forms import BetForm, RaceForm
from .models import Driver, Race, Track


# Create your views here.
# http://localhost:8081/nascar/
def index(request):
    return HttpResponse("Hello World from nascar!")


# http://localhost:8081/nascar/tracks
def tracks(request):
    list_of_tracks = Track.objects.order_by("track_name")
    context = {"list_of_tracks": list_of_tracks}
    return render(request, "nascar/tracks.html", context=context)


def race(request):
    form = RaceForm()
    races = Race.objects.all()
    context = {"races": races}
    context = {"title": "2024 Nascar Races"}
    context = {"form": form}
    return render(request, "race.html", context=context)


# http://localhost:8081/nascar/races
def races(request):
    list_of_races = Race.objects.order_by("track", "race_date")
    context = {"list_of_races": list_of_races}
    return render(request, "nascar/races.html", context=context)


# http://localhost:8081/nascar/drivers
def drivers(request):
    list_of_drivers = Driver.objects.order_by("name")
    context = {"list_of_drivers": list_of_drivers}
    return render(request, "nascar/drivers.html", context=context)


# https://ordinarycoders.com/blog/article/render-a-django-form-with-bootstrap
# https://ordinarycoders.com/blog/article/django-models
# https://stackoverflow.com/questions/75495403/django-returns-templatedoesnotexist-when-using-crispy-forms
# pip install crispy-forms
# pip install crispy-bootstrap4
# make sure they are in the installed_apps section of the settings file
def bets(request):
    form = BetForm()
    return render(request, "nascar/bets.html", {"form": form})
