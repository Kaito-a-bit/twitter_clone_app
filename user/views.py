
from dataclasses import fields
from pyexpat import model
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from user.models import User
from .forms import SignUpForm


class BaseView(TemplateView):
    template_name = 'user/top.html'


class HomeView(TemplateView):
    template_name = 'user/home.html'
    

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'user/sign_up.html'
    success_url = reverse_lazy('user:home')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url()) 



