from django.urls import path
from .views import home

urlpatterns = [
    # path("spltxt/", AjaxTxtView.as_view(), name="ajax-sampletxt"),
    # path("spljson/", AjaxJsonView.as_view(), name="ajax-samplejson"),
    # path("teams/", TeamsFrontendView.as_view(), name="teams-frontend"),
    path("index/", home, name="index"),
]
