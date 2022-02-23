
from dataclasses import fields
import email
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
        response = super().form_valid(form) #ここでフォームの情報を保存
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        birthday = form.cleaned_data.get('birthday')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        self.object = user #これは何
        login(self.request, self.object)
        return response


