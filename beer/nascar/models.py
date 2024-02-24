# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from ast import mod
from email.policy import default

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Base(models.Model):
    now = timezone.datetime
    date_created = models.DateTimeField("date created", auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_updated = models.DateTimeField("date last updated", auto_now=True, null=True)

    class Meta:
        abstract = True


class Bet(Base):
    player = models.ForeignKey(
        "Player", models.DO_NOTHING, db_column="PLAYER_ID", blank=True, null=True
    )  # Field name made lowercase.
    race = models.ForeignKey(
        "Race", models.DO_NOTHING, db_column="RACE_ID", blank=True, null=True
    )  # Field name made lowercase.
    # track = models.ForeignKey(
    #     "Track", models.DO_NOTHING, db_column="TRACK_ID", blank=True, null=True
    # )  # Field name made lowercase.
    driver = models.ForeignKey(
        "Driver",
        models.DO_NOTHING,
        db_column="DRIVER_ID",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    bet_id = models.AutoField(
        db_column="BET_ID", primary_key=True
    )  # Field name made lowercase.
    finish = models.IntegerField(null=False, default=0, db_column="Race Finish")
    first_pick = models.BooleanField(default=False, null=False)

    class Meta:
        # managed = False
        db_table = "bet"
        unique_together = (
            (
                "player",
                "first_pick",
                "race",
            ),
        )


class Driver(Base):
    driver_id = models.AutoField(
        db_column="DRIVER_ID", primary_key=True
    )  # Field name made lowercase.
    name = models.CharField(
        db_column="NAME", unique=True, max_length=32
    )  # Field name made lowercase.
    car_no = models.IntegerField(
        db_column="CAR_NO", blank=True, null=True
    )  # Field name made lowercase.
    sponsor = models.CharField(
        db_column="SPONSOR", max_length=64, blank=True, null=True
    )  # Field name made lowercase.
    make = models.CharField(
        db_column="MAKE", max_length=32, blank=True, null=True
    )  # Field name made lowercase.
    team = models.CharField(
        db_column="TEAM", max_length=64, blank=True, null=True
    )  # Field name made lowercase.
    salary = models.IntegerField(
        db_column="SALARY", blank=True, null=True
    )  # Field name made lowercase.
    starting_position = models.IntegerField(
        db_column="STARTING_POSITION", blank=True, null=True
    )  # Field name made lowercase.

    def __unicode__(self):
        return self.name

    def __str__(self) -> str:
        return self.name

    class Meta:
        # managed = False
        db_table = "driver"
        unique_together = (("name", "team", "car_no"),)


class Player(Base):
    player_id = models.AutoField(
        db_column="PLAYER_ID", primary_key=True
    )  # Field name made lowercase.
    player_name = models.CharField(
        db_column="PLAYER_NAME", max_length=32
    )  # Field name made lowercase.

    def __str__(self) -> str:
        return self.player_name

    class Meta:
        # managed = False
        db_table = "player"


class Race(Base):
    race_id = models.AutoField(
        db_column="RACE_ID", primary_key=True
    )  # Field name made lowercase.
    race_name = models.CharField(
        db_column="RACE_NAME", max_length=64
    )  # Field name made lowercase.
    race_date = models.DateField(db_column="RACE_DATE")  # Field name made lowercase.
    track = models.ForeignKey(
        "Track", models.DO_NOTHING, db_column="TRACK_ID", blank=True, null=True
    )  # Field name made lowercase.
    track_name = models.CharField(
        db_column="TRACK_NAME", max_length=64
    )  # Field name made lowercase.

    def __str__(self) -> str:
        return f"{self.race_name}"

    class Meta:
        # managed = False
        db_table = "race"
        unique_together = (("race_date", "race_name"),)


class Results(Base):
    driver = models.ForeignKey(
        Driver, models.DO_NOTHING, db_column="DRIVER_ID", blank=True, null=True
    )  # Field name made lowercase.
    race = models.ForeignKey(
        Race, models.DO_NOTHING, db_column="RACE_ID", blank=True, null=True
    )  # Field name made lowercase.
    results_id = models.AutoField(
        db_column="RESULTS_ID", primary_key=True
    )  # Field name made lowercase.
    position = models.IntegerField(db_column="POSITION")  # Field name made lowercase.
    car = models.IntegerField(db_column="CAR")  # Field name made lowercase.
    manufacturer = models.CharField(
        db_column="MANUFACTURER", max_length=64
    )  # Field name made lowercase.
    start = models.IntegerField(db_column="START")  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = "results"
        unique_together = (("driver", "race"),)


class Track(Base):
    """TRACK,OWNER,MILES,CONFIG,CITY,STATE

    Args:
        Base (_type_): _description_
    """

    name = models.CharField(max_length=64, default="N/A", null=False)
    owner = models.CharField(max_length=64, default="N/A")
    track_length = models.FloatField(default=0.0, null=False)
    configuration = models.CharField(max_length=32, default="Oval", null=False)
    city = models.CharField(max_length=64, null=False, default="N/A")
    state = models.CharField(max_length=64, null=False, default="N/A")

    class Meta:
        models.UniqueConstraint(fields=["name"], name="unique_track_name")

    def __str__(self) -> str:
        return f"{self.name} {self.track_length} - {self.configuration}"
