from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tracks/", views.tracks, name="tracks"),
    path("races/", views.races, name="races"),
    path("drivers/", views.drivers, name="drivers"),
    path("bets/", views.bets, name="bets"),
]
