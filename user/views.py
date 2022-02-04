from http.client import HTTPResponseRedirect
from django.contrib.auth import login
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .forms import SignUpForm

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'sign_up.html'
    # success_url = reverse_lazy(ログイン成功時のurl)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return HTTPResponseRedirect(self.get_success_url()) 

class HomeView(TemplateView):
    template_name='base.html'
