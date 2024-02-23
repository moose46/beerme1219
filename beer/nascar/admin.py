from django.contrib import admin
from nascar.models import Driver, Race, Results, Track

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
    list_display = ("race", "driver", "car")
    # autocomplete_fields = ["driver"]


# @admin.register(Race)
# class RaceAdmin(admin.ModelAdmin):
#     list_display = ("race_name", "race_date", "track_name")


# admin.site.register(Results)
# admin.site.register(TeamDriver)
# admin.site.register(Team)
