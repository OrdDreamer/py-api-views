from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    GenreListCreateAPIView,
    GenreRetrieveUpdateDestroyAPIView,
    ActorListCreateView,
    ActorRetrieveUpdateDestroyView,
    CinemaHallViewSet,
    MovieViewSet,
)

router = DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet, basename="cinema-hall")
router.register("movies", MovieViewSet, basename="movie")

urlpatterns = [
    path("genres/", GenreListCreateAPIView.as_view(), name="genre-list"),
    path(
        "genres/<int:pk>/",
        GenreRetrieveUpdateDestroyAPIView.as_view(),
        name="genre-detail"
    ),
    path("actors/", ActorListCreateView.as_view(), name="actor-list"),
    path(
        "actors/<int:pk>/",
        ActorRetrieveUpdateDestroyView.as_view(),
        name="actor-detail"
    ),
    path("", include(router.urls)),
]

app_name = "cinema"
