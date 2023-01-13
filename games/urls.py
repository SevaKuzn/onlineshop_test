from django.contrib import admin
from django.urls import path, include
from games.views import home
from games.views import GameListView

urlpatterns = [
    path('',GameListView.as_view() ,name='home'),
]
