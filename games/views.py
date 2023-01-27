from django.shortcuts import render
from django.views.generic import ListView, DetailView
from games.models import Game
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    return render(request,'home.html')

class GameListView(ListView):
    model = Game
    template_name = 'games/home.html'
    context_object_name = 'game_list'

class GameDetailView(LoginRequiredMixin, DetailView):
    model = Game
    context_object_name = 'game'