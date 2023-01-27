from django.shortcuts import render
from django.views.generic import CreateView
from accounts.forms import UserSignUpForm
from django.urls import reverse_lazy

# Create your views here.
class UserCreationView(CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/sign_up.html'