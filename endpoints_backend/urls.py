from django.urls import path
from rest_framework import routers
from .api import CommentViewSet
from .views import users, pokemonByName, pokemonId, characterList, locationById
from django.views.decorators.csrf import csrf_exempt

router = routers.DefaultRouter()
router.register("api/comment", CommentViewSet, "comments")

urlpatterns = [
    path("users", users, name="users"),
    path("pokemonByName", pokemonByName, name="pokemon by name"),
    path("pokemonId/<str:id>", pokemonId, name="Pokemon By id"),
    path("characters", characterList, name="List of characters Rick and Morty"),
    path("location/<str:id>", locationById, name="Location by id")
]
