
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from tweet import forms
from tweet.forms import TweetForm
from .import forms

class TweetView(CreateView):
    template_name = 'tweet/posting.html'
    form_class = TweetForm
    success_url = reverse_lazy('user:home')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        print(form.instance.created_at)
        return super().form_valid(form)
        
