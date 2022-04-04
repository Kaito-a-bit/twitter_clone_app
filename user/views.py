
from asyncio import as_completed
from re import template
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden, HttpResponseRedirect
from user.models import ConnectionModel, User
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

class ProfileView(ListView):
    template_name = "user/profile.html"
    model = Tweet

    def get_queryset(self):
        associated_id = self.kwargs['pk']
        user = User.objects.get(id=associated_id)
        return Tweet.objects.filter(author=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        associated_id = self.kwargs['pk']
        context["author"] = User.objects.filter(id=associated_id).first()
        return context

def follow_view(request, pk):
    try:
        follower = User.objects.get(username=request.user.username)
        following = User.objects.get(id=pk)
    except User.DoesNotExist:
        messages.warning(request, '{}は存在しません')
        return HttpResponseRedirect(reverse_lazy('user:profile'))

    if follower == following:
        messages.warning(request, '自分自身はフォローできません。')
    else:
        _, created = ConnectionModel.objects.get_or_create(follower=follower, following=following)

        if created:
                messages.success(request, '{}をフォローしました'.format(following.username))
        else:
            messages.warning(request, 'あなたはすでに{}をフォローしています'.format(following.username))

    return HttpResponseRedirect(reverse_lazy('user:home'))

