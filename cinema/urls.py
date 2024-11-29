from django.urls import path, include
from rest_framework import routers
from cinema.views import (MovieViewSet,
                          GenreList,
                          GenreDetail,
                          CinemaHallViewSet, ActorList, ActorDetail)

router = routers.DefaultRouter()
router.register("movie", MovieViewSet)

cinema_hall_list = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create",
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
    path("genre/",
         GenreList.as_view(),
         name="genre_list"),
    path("genre/<int:pk>/",
         GenreDetail.as_view(),
         name="genre-detail"),
    path("cinema_hall/",
         cinema_hall_list,
         name="cinema_hall_list"),
    path("cinema_hall/<int:pk>/",
         cinema_hall_detail,
         name="cinema_hall_detail"),
    path("actor/",
         ActorList.as_view(),
         name="actor_list"),

    path("actor/<int:pk>/",
         ActorDetail.as_view(),
         name="actor-detail")
]

app_name = "cinema"
