from .models import Team, Player
from .serializers import TeamSerializer, PlayerSerializer, PlayersSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404


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
    serializer_class = PlayerSerializer

    def get(self, request):
        player = Player.objects.all()
        serializers = PlayersSerializer(player, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
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
