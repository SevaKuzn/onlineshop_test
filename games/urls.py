from django.contrib import admin
from django.urls import path, include
from games.views import home
from games.views import GameListView, GameDetailView

urlpatterns = [
    path('',GameListView.as_view() ,name='home'),
    path('<slug:slug>/', GameDetailView.as_view(), name='game_detail'),
]
