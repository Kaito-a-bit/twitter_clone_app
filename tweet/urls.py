
from django.urls import path
from . import views

app_name = 'tweet'
urlpatterns = [
  path('posting/', views.TweetView.as_view(), name = 'tweet')
]
