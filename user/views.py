
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from .forms import SignUpForm
from tweet.models import Tweet

class TopView(TemplateView):
    template_name = 'user/top.html'


class HomeView(LoginRequiredMixin, ListView):
    template_name = 'user/home.html'
    login_url = 'login'
    model = Tweet
    

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'user/sign_up.html'
    success_url = reverse_lazy('user:home')

    def form_valid(self, form):
        response = super().form_valid(form) #ここでフォームの情報を保存
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=email, password=password)
        if user is not None:
            login(self.request, user)
            return response
        else:
            print("user is none")
            print(password)
            print(email)
            return HttpResponseForbidden()
