from django.urls import path
from .views import (
    TournmentListViews,
    TournmentDetailView,
    ParticipationListView,
    ParticipationDetailView,
)

urlpatterns = [
    path("", TournmentListViews.as_view(), name="tournment-list"),
    path("<int:id>/", TournmentDetailView.as_view(), name="tournment-detail"),
    path("participation/", ParticipationListView.as_view(), name="participation-list"),
    path(
        "participation/<int:id>/",
        ParticipationDetailView.as_view(),
        name="participation-detail",
    ),
]
