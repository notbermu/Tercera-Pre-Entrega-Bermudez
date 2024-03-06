from django.urls import path
from PageApp import views

urlpatterns = [
    path('', views.HomeView, name="Home"),
    path('Songs/', views.SongsView, name="Songs"),
    path('Players/', views.PlayersView, name="Players"),
    path('Movies/', views.MoviesView, name="Movies"),
    path('SearchPlayers/', views.SearchPlayers)
]
    