from urllib import response

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from matplotlib import widgets

from .forms import BetForm, RaceDeleteForm, RaceIndexForm
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


# path("race/", views.race_index, name="race_index"),
# http://127.0.0.1:8081/nascar/race/
def race_index(request):
    if request.method == "POST":
        data = request.POST
        print(f"race_index:POST {request}")
        print(f"{data.get('race')}")
        race_delete_form = RaceDeleteForm()
        races = Race.objects.all()
        return render(
            request,
            "nascar/race/delete.html",
            context={"form": race_delete_form, "races": races},
        )
    else:
        print("race_index !POST")
    # get all races and order them by the race date
    races = Race.objects.all().order_by("race_date")
    context = {
        "races": races,
        "debug_info": "2024 Nascar Races! (views/race_index) render(nascar/race/index.html)",
        # "form": form,
    }
    # print("race_index")
    return render(request, "nascar/race/index.html", context=context)


# path("race/create/", views.race_create, name="race_create"),
# http://127.0.0.1:8081/nascar/race/create/
def race_create(request):
    if request.method == "POST":
        if "Create" in request.POST:
            form = RaceIndexForm(request.POST)
            if form.is_valid():
                n = form.cleaned_data["race_name"]
                t = form.cleaned_data["track"]
                d = form.cleaned_data["race_date"]
                print(f"{d} - {n} - {t}")
                race = Race(race_name=n)
                race.race_date = d
                race.track = t
                race.race_name = n
                race.user = User.objects.get(pk=1)
                track = Track.objects.get(track_name=t)
                print(track)
                race.track = track
                race.save()
                # return to the list of races page
                return HttpResponseRedirect("../../race")
        elif "Delete" in request.POST:
            print("Delete Races")
    else:
        print("return else")
        form = RaceIndexForm()
        context = {
            "form": form,
            "debug_info": f"{__name__} path(race/create/, views.race_create, name=race_create) - /nascar/race/create.html",
        }
        return render(request, "nascar/race/create.html", context=context)


def debug(function_name):
    print(f"{function_name.__name__}")


def race_delete(request):
    form = RaceDeleteForm()
    races = Race.objects.all()
    if request.method == "POST":
        print("race_delete POST")
    else:
        print(f"race_delete = {__file__} / {__name__} / {request}")
    # "debug_info": f"{__name__} path(race/create/, views.race_create, name=race_create) - /nascar/race/create.html",
    return render(
        request, "nascar/race/delete.html", context={"form": form, "races": races}
    )


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
