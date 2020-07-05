from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Player, Team
from .serializers import (
    PlayerSerializer,
    PlayersSerializer,
    TeamSerializer,
    UserSerializer,
)

User = get_user_model()


class TeamListApiView(APIView):
    # give permission only to create admins and superuser
    def get(self, request):
        team = Team.objects.all()
        serializers = TeamSerializer(team, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamDetailApiView(APIView):
    def get_object(self, id=None):
        return get_object_or_404(Team, id=id)

    def get(self, request, id=None):
        team = self.get_object(id=id)
        serializer = TeamSerializer(team)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id=None):
        team = self.get_object(id=id)
        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        team = self.get_object(id=id)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PlayerListView(APIView):
    def get(self, request):
        player = Player.objects.all()
        serializers = PlayersSerializer(player, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        # changed to PlayersSerializer and in ser.save(user=request.user)
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlayerDetailView(APIView):
    def get_object(self, id=None):
        return get_object_or_404(Player, id=id)

    def get(self, request, id=None):
        player = self.get_object(id=id)
        serializer = PlayersSerializer(player)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id=None):
        player = self.get_object(id=id)
        serializer = PlayerSerializer(player, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        player = self.get_object(id=id)
        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UsersViewList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDetailView(APIView):
    def get_object(self, id=None):
        return get_object_or_404(User, id=id)

    def get(self, request, id=None):
        user = self.get_object(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
