from rest_framework import serializers

from .models import Tournment, Participation


class TournmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournment
        fields = ["id", "tournment_name", "members"]


class ParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participation
        fields = ["id", "tournment", "user", "note"]


class ParticipationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participation
        fields = ["id", "tournment", "note"]
