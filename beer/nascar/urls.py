from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tracks/", views.tracks, name="tracks"),
    # path("races/", views.race_index, name="race_index"),
    path("drivers/", views.drivers, name="drivers"),
    path("bets/", views.bets, name="bets"),
    path("race_index/", views.race_index, name="race_index"),
    # path("race/", views.race_index, name="race_index"),
    # path("race/create/", views.race_create, name="race_create"),
    path("race/delete/", views.race_delete, name="race_delete"),
    path("race_edit", views.race_edit, name="race_edit"),
]
