from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
  path('',views.TopView.as_view(), name='top'),
  path('signup/',views.SignUpView.as_view(), name='signup'),  
  path('home/', views.HomeView.as_view(), name='home'),
  path('home/<int:pk>', views.ProfileView.as_view(), name='profile'),
  path('home/<int:pk>/follow', views.follow_view, name='follow'),
  path('home/<int:pk>/unfollow', views.unfollow_view, name='unfollow'),
  path('like/<uuid:pk>/', views.LikeView, name='like')
]
