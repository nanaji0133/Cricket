from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response


# class AjaxTxtView(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = "frontend/ajax1.html"

#     def get(self, request):
#         return Response({})


# class AjaxJsonView(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = "frontend/ajax2.html"

#     def get(self, request):
#         return Response({})


class TeamsFrontendView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "frontend/team/team.html"

    def get(self, request):
        return Response({})
