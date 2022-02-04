from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
  path('',views.HomeView.as_view(), name='base'),
  path('signup/',views.SignUpView.as_view(), name='signup'),  
]
