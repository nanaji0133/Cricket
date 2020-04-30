from django.shortcuts import render, get_object_or_404

from .serializers import (
    TournmentSerializer,
    ParticipationSerializer,
    ParticipationUserSerializer,
)
from .models import Tournment, Participation

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TournmentListViews(APIView):
    def get(self, request):
        tournment = Tournment.objects.all()
        serializer = TournmentSerializer(tournment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TournmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TournmentDetailView(APIView):
    def get_object(self, id=None):
        return get_object_or_404(Tournment, id=id)

    def get(self, request, id=None):
        tournment = self.get_object(id=id)
        serializer = TournmentSerializer(tournment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id=None):
        tournment = self.get_object(id=id)
        serializer = TournmentSerializer(tournment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        tournment = self.get_object(id=id)
        tournment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ParticipationListView(APIView):
    def get(self, request):
        participation = Participation.objects.all()
        serializer = ParticipationSerializer(participation, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ParticipationUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ParticipationDetailView(APIView):
    def get_object(self, id=None):
        return get_object_or_404(Participation, id=id)

    def get(self, request, id=None):
        participation = self.get_object(id=id)
        serializer = ParticipationSerializer(participation)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id=None):
        participation = self.get_object(id=id)
        serializer = ParticipationUserSerializer(participation, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        participation = self.get_object(id=id)
        participation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
