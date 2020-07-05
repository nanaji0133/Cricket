from django.urls import path

from .views import (
    PlayerDetailView,
    PlayerListView,
    TeamDetailApiView,
    TeamListApiView,
    UsersViewList,
    UserDetailView
)

urlpatterns = [
    path("", TeamListApiView.as_view(), name="teams"),
    path("<int:id>/", TeamDetailApiView.as_view(), name="team-detail"),
    path("players/", PlayerListView.as_view(), name="players"),
    path("players/<int:id>/", PlayerDetailView.as_view(), name="player-detail"),
    path("users/", UsersViewList.as_view(), name="users-list"),
    path("users/<int:id>/", UserDetailView.as_view(), name="user-detail")
]
