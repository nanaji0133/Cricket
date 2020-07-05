from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Player, Team

User = get_user_model()


class TeamSerializer(serializers.ModelSerializer):
    players = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ["id", "team_name", "team_rank", "players"]


class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["id", "user", "country", "style", "team"]


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["id", "country", "style", "team"]


class UserSerializer(serializers.ModelSerializer):
    # player = PlayerSerializer(read_only=True)

    class Meta:
        model = User
        fields = ["id", "username"]
