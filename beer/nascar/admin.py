from django.contrib import admin
from nascar.models import Bet, Driver, Player, Race, Results, Track

# Register your models here.


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("name", "car_no")
    ordering = ["name"]


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ("name", "configuration", "track_length", "city", "state")


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


@admin.register(Bet)
class BetAdmin(admin.ModelAdmin):
    list_display = (
        "player_name",
        "first_pick",
        "track_name",
        "race_date",
        "driver",
        "finish",
    )
    # ordering = [
    #     "race_date",
    # ]
    # BUG: odering
    # TODO: add race date ordering

    def race_date(self, instance):
        return f"{instance.race.race_date} / {instance.race.track_name}"

    def track_name(self, instance):
        return instance.race.track

    def driver(self, instance):
        return instance.driver.name

    def player_name(self, instance):
        return f"{instance.player.player_name}"


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = (
        "race_name",
        "race_date",
        "track_track_name",
    )

    def track_track_name(self, instance):
        return f"{instance.track}"


# @admin.register(Race)
# class RaceAdmin(admin.ModelAdmin):
#     list_display = ("race_name", "race_date", "track_name")


# admin.site.register(Results)
# admin.site.register(TeamDriver)
# admin.site.register(Team)
