from django.urls import path, include
from rest_framework import routers
from cinema.views import (MovieViewSet,
                          GenreList,
                          GenreDetail,
                          CinemaHallViewSet)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

cinema_hall_list = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create"
    }
)

cinema_hall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)
urlpatterns = [
    path("",
         include(router.urls)),
    path("genres/",
         GenreList.as_view(),
         name="genre_list"),
    path("genres/<int:pk>/",
         GenreDetail.as_view(),
         name="genre-detail"),
    path("cinema-hall/",
         cinema_hall_list,
         name="cinema_hall_list"),
    path("cinema-hall/<int:pk>/",
         cinema_hall_detail,
         name="cinema_hall_detail"),
]

app_name = "cinema"
