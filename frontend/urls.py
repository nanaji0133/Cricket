from django.urls import path
from .views import AjaxTxtView, AjaxJsonView

urlpatterns = [
    path("spltxt/", AjaxTxtView.as_view(), name="ajax-sampletxt"),
    path("spljson/", AjaxJsonView.as_view(), name="ajax-samplejson"),
    
]
