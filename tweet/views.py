from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from tweet.forms import TweetForm

class TweetView(CreateView):
    template_name = 'tweet/posting.html'
    form_class = TweetForm
    success_url = reverse_lazy('user:home')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
