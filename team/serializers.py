from .models import Team, Player

from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()


class TeamSerializer(serializers.ModelSerializer):
    players = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ["id", "team_name", "team_rank", "players"]


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["id", "user", "country", "style", "team"]


class UserSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "player"]

