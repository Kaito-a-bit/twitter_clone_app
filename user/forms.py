from cProfile import label
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'birthday', 'password')
        labels = {
            'username': 'ユーザネーム',
            'email': 'email',            
            'birthday': '誕生日',
            'password': 'パスワード'
        }
        help_texts = {
            'username': '名前を入力してください（最大24文字）',
            'email': 'メールアドレスを入力してください',
            'birthday': '誕生日を入力してください（例: 1999-1-1）',
            'password': 'パスワードを入力してください'
        }
