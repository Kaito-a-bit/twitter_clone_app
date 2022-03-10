
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
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
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('passsword1')
        user = authenticate(username=email, password=password)
        if user is not None:
            login(self.request, user)
            return response
        else:
            print("user is none")
            print(password)
            print(email)
            return HttpResponseForbidden()
