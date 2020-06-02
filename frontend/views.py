from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response


def home(request):
    return render(request, "frontend/index.html")
