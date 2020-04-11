from django.db import models

from django.conf import settings

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Player(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    country = models.CharField(max_length=20, blank=True, null=True)
    style = models.CharField(max_length=20, default="batsmen")
    team = models.ForeignKey("Team", on_delete=models.CASCADE, related_name="players")

    def __str__(self):
        return f"{self.user} in team {self.team}"


class Team(models.Model):
    team_name = models.CharField(max_length=20, blank=False, null=False)
    team_rank = models.IntegerField(blank=True, null=True, unique=True)

    def __str__(self):
        return f"{self.team_name}"
