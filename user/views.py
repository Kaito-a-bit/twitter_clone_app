
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy, reverse
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
        profile_user_id = self.kwargs['pk']
        user = User.objects.get(id=profile_user_id)
        return Tweet.objects.filter(author=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_user_id = self.kwargs['pk']
        context["author"] = User.objects.filter(id=profile_user_id).first()
        context["requesting_user"] = self.request.user
        return context

def follow_view(request, pk):
    try:
        follower = User.objects.get(username=request.user.username)
        following = User.objects.get(id=pk)
        if follower == following:
            messages.add_message(request, messages.ERROR, "自分をフォローすることはできません。")
        else:
            _, created = ConnectionModel.objects.get_or_create(follower=follower, following=following)
            if created:
                messages.add_message(request, messages.SUCCESS, "ユーザをフォローしました")
            else:
                messages.add_message(request, messages.ERROR, "あなたはすでにこのユーザをフォローしています")
    except User.DoesNotExist:
        messages.add_message(request, messages.ERROR, "ユーザが存在しません")
    url = reverse('user:profile', kwargs={'pk': pk })
    return HttpResponseRedirect(url)
    
def unfollow_view(request, pk):
    try:
        follower = User.objects.get(username=request.user.username)
        following = User.objects.get(id=pk)
        if follower == following:
            messages.add_message(request, messages.ERROR, "自分自身のフォローを外すことはできません。")
        else:
            target = ConnectionModel.objects.filter(follower=follower, following=following)
            if target.exists():
                target.delete()
                messages.add_message(request, messages.SUCCESS, "このユーザのフォローを外しました")
            else:
                messages.add_message(request, messages.ERROR, "まだあなたはこのユーザをフォローしていません。")
    except User.DoesNotExist:
        messages.add_message(request, messages.ERROR, "このユーザは存在しません。")
    url = reverse('user:profile', kwargs={'pk': following.pk })
    return HttpResponseRedirect(url)
