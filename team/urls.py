from django.urls import path
from .views import TeamListApiView, TeamDetailApiView, PlayerListView, PlayerDetailView

urlpatterns = [
    path("", TeamListApiView.as_view(), name="teams"),
    path("<int:id>/", TeamDetailApiView.as_view(), name="team-detail"),
    path("players/", PlayerListView.as_view(), name="players"),
    path("players/<int:id>/", PlayerDetailView.as_view(), name="player-detail"),
]
