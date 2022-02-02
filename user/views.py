from http.client import HTTPResponse
from django.shortcuts import render
from django.views.generic import TemplateView

class SignupView(TemplateView):
    template_name = "user/sign_up.html"
