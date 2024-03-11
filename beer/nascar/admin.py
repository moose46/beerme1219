from django.contrib import admin
from nascar.models import Bet, Driver, Manufacturer, Player, Race, Results, Team, Track

# Register your models here.


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_filter = ["team_fk"]
    list_display = ("name", "car_no")
    ordering = ["name"]


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ("track_name", "configuration", "track_length", "city", "state")


class ChoiceAdmin(admin.ModelAdmin):
    autocomplete_fields = ["driver"]


@admin.register(Results)
class ResultsAdmin(admin.ModelAdmin):
    list_display = (
        "race",
        "driver",
        "car",
    )
    # autocomplete_fields = ["driver"]


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("player_name",)


@admin.register(Manufacturer)
class TeamManufacturer(admin.ModelAdmin):
    list_display = ["manufacturer_name"]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ["team_name", "manufacturer_name"]
    list_filter = ["manufacturer"]
    ordering = ["team_name"]

    def manufacturer_name(self, instance):
        return f"{instance.manufacturer.manufacturer_name}"


@admin.register(Bet)
class BetAdmin(admin.ModelAdmin):
    list_display = (
        "player_name",
        "driver",
        "race_date",
        "track_name",
        "finish",
        "first_pick",
    )
    ordering = [
        "race_fk__race_date",
        "player_fk__player_name",
    ]

    # def race_race_date(self, instance):
    #     return instance.race_fk.race_date

    # # TODO: add race date ordering

    def race_date(self, instance):
        return f"{instance.race_fk.race_date} / {instance.race_fk.track_fk}"

    def track_name(self, instance):
        return instance.race_fk.track_fk

    def driver(self, instance):
        return instance.driver_fk.name

    def player_name(self, instance):
        return f"{instance.player_fk.player_name}"


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    # date_hierarchy = "race_date"
    # list_filter = ["track_fk__track_name"]
    list_display = (
        "race_date",
        # "track_fk_track_name",
        "race_name",
    )
    ordering = ["-race_date"]

    # def track_track_name(self, instance):
    #     return f"{instance.track_name}"
