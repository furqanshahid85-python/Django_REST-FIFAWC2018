from django.urls import path

from .views import ListAllPlayers, RetrievePlayer, AddNewPlayer, UpdatePlayer, DeletePlayer


urlpatterns = [
    path("allplayers", ListAllPlayers.as_view(), name="players_list"),
    path("player/<int:pk>", RetrievePlayer.as_view(), name="player_data"),
    path("addplayer", AddNewPlayer.as_view(), name="add_player"),
    path("updateplayer/<int:pk>", UpdatePlayer.as_view(), name="update_player"),
    path("deleteplayer/<int:pk>", DeletePlayer.as_view(), name="delete_player"),

]
