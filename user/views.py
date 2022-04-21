from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from user.models import ConnectionModel, User
from django.db.models import Prefetch, Count
from .forms import SignUpForm
from tweet.models import Tweet, Like

class TopView(TemplateView):
    template_name = 'user/top.html'


class HomeView(LoginRequiredMixin, ListView):
    template_name = 'user/home.html'
    login_url = 'login'
    queryset = Tweet.objects.select_related('author')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tweets = Tweet.objects.prefetch_related(Prefetch('like_tweets', queryset=Like.objects.filter(user=self.request.user), to_attr="user_like_set")).annotate(user_like_count=Count('like_tweets')).all()
        liked_list = []
        for tweet in tweets:
            # aggregateの数値で分岐
            if tweet.user_like_count == 0:
                liked_list.append(tweet.id)
        context["user_fav_list"] = liked_list
        return context


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
        user = get_object_or_404(User,id=profile_user_id)
        return Tweet.objects.filter(author=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_user_id = self.kwargs['pk']
        context["author"] = get_object_or_404(User,id=profile_user_id)
        return context

@login_required
def follow_view(request, pk):
    try:
        follower = request.user
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
    
@login_required
def unfollow_view(request, pk):
    try:
        follower = request.user
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

def like_view(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    user = request.user
    liked = False
    like = Like.objects.filter(tweet=tweet, user=user)
    if like.exists():
        like.delete()
    else:
        Like.objects.create(tweet=tweet, user=user)
        liked = True
    context = {
        'tweet_id': tweet.id,
        'liked': liked,
        'count': tweet.like_tweets.count(),
    }
    return JsonResponse(context)
