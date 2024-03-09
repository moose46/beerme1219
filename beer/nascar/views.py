# from django import template

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

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
