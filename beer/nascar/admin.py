from django.contrib import admin
from nascar.models import (
    Bet,
    Bets,
    Driver,
    Manufacturer,
    Player,
    Race,
    RaceBet,
    Results,
    Team,
    Track,
)

# Register your models here.


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_filter = ["team"]
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
        "car_no",
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


@admin.register(RaceBet)
class RaceBetAdmin(admin.ModelAdmin):
    pass


@admin.register(Bets)
class BetsAdmin(admin.ModelAdmin):
    pass


@admin.register(Bet)
class BetAdmin(admin.ModelAdmin):
    list_display = (
        "player_name",
        "driver",
        "race_date",
        "track_name",
        "finish_position",
        "first_pick",
    )
    ordering = [
        "race__race_date",
        "player__player_name",
    ]

    # def race_race_date(self, instance):
    #     return instance.race_fk.race_date

    # # TODO: add race date ordering

    def race_date(self, instance):
        return f"{instance.race.race_date} / {instance.race.track}"

    def track_name(self, instance):
        return instance.race.track

    def driver(self, instance):
        return instance.driver.name

    def player_name(self, instance):
        return f"{instance.player.player_name}"


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    # date_hierarchy = "race_date"
    list_filter = ["track"]
    list_display = (
        "race_date",
        # "track_fk_track_name",
        "race_name",
    )
    ordering = ["-race_date"]

    # def track_track_name(self, instance):
    #     return f"{instance.track_name}"
