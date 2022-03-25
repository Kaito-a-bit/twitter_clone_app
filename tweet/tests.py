from django.test import TestCase
from django.urls import reverse
from .models import Tweet
from user.models import User

class PostingViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@gmail.com', password= 'ttt019283est')

    def test_get_success(self):
        self.client.login(username="test@gmail.com", password="ttt019283est")

        data = {
          'text': 'testtext',
          'author': 'test@gmail.com',
          'created_at': '2022-03-25 17:10:39+09:00',
        }
        self.response = self.client.post(reverse('tweet:tweet'), data)
        self.assertRedirects(self.response, reverse('user:home'))

