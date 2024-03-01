"""
    Reads drivers.csv file and imports drivers into the drivers table.
    If there are duplicates, it will stop, and throw up
    must have django-extensions installed and in entered into the INSTALLED_APPS settings file.
    
        INSTALLED_APPS = [
            "nascar.apps.NascarConfig",
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "django.contrib.staticfiles",
            "django_extensions",
        ]

    to run:
        python manage.py runscript load_tracks_from_csv
"""

import csv
import datetime
import os
import sys
from collections import namedtuple
from datetime import date
from pathlib import Path

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from ..models import Race, Track

# https://k0nze.dev/posts/python-relative-imports-vscode/


def makeDate(pdate: list):
    """Create a date suitable for the database from a list"""
    if pdate[0] == "Feb.":
        return f"2022-02-{pdate[1]}"
    elif pdate[0] == "March":
        return f"2022-03-{pdate[1]}"
    elif pdate[0] == "April":
        return f"2022-04-{pdate[1]}"
    elif pdate[0] == "May":
        return f"2022-05-{pdate[1]}"
    elif pdate[0] == "June":
        return f"2022-06-{pdate[1]}"
    elif pdate[0] == "July":
        return f"2022-07-{pdate[1]}"
    elif pdate[0] == "Aug.":
        return f"2022-08-{pdate[1]}"
    else:
        return pdate


def run():
    user = User.objects.get(pk=1)
    # with open(Path.cwd() / "scripts" / "tracks.csv") as f:
    with open(Path.cwd() / "2023-nascar-schedule.txt") as f:
        f_csv = csv.reader(f, delimiter="\t")
        headers = next(f_csv)
        # TRACK,OWNER,MILES,CONFIG,CITY,STATE
        Row = namedtuple("Row", headers)

        for row in f_csv:
            # print(row)
            try:
                row = Row(*row)
            except Exception as e:
                print(e)
                exit()
            race_date = row.Date
            print(makeDate(race_date.split()))
            race = Race()
            # race.race_date = race_date
            # lookup track id
            track = Track()
            track = Track()
            if Track.objects.filter(name=row.Track):
                track = Track.objects.get(name=row.Track)
            else:
                print(f"{row.Track} Poop!")
                continue

            race.track = track
            print(race.track)
            race.race_name = row.Race
            race.race_date = makeDate(race_date.split())
            race.user = user
            try:
                race.save()
            except Exception as e:
                print(e)
                continue
