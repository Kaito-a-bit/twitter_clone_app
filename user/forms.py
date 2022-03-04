from django.contrib.auth.forms import UserCreationForm
from cProfile import label
from django import forms
from .models import User

class SignUpForm(UserCreationForm):
   
    class Meta:
        model = User
        fields = ('username', 'email', 'birthday')

        labels = {
            'username': 'ユーザネーム',
            'email': 'email',            
            'birthday': '誕生日',
        }
        help_texts = {
            'username': '名前を入力してください（最大24文字）',
            'email': 'メールアドレスを入力してください',
            'birthday': '誕生日を入力してください（例: 1999-1-1）',
        }
