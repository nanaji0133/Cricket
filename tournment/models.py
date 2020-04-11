from django.db import models
from django.conf import settings


class Tournment(models.Model):
    tournment_name = models.CharField(max_length=20)
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through="Participation",
        through_fields=("tournment", "user"),
        related_name="tournments",
        symmetrical=True,
    )
    joined_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tournment_name}"


class Participation(models.Model):
    tournment = models.ForeignKey(Tournment, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    note = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"participation of {self.user} in {self.tournment}"
