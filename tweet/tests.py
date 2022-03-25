from django.test import TestCase
from django.urls import reverse
from .models import Tweet
from user.models import User

class PostingViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@gmail.com', password= 'ttt019283est')
        self.client.login(username="test@gmail.com", password="ttt019283est")

    def test_get_success(self):
        data = {
          'text': 'testtext',
          'author': 'test@gmail.com',
          'created_at': '2022-03-25 17:10:39+09:00',
        }
        self.response = self.client.post(reverse('tweet:tweet'), data)
        self.assertRedirects(self.response, reverse('user:home'))

    def test_post_creation(self):
        data = {
          'text': 'testtext',
          'author': 'test@gmail.com',
          'created_at': '2022-03-25 17:10:39+09:00',
        }
        self.response = self.client.post(reverse('tweet:tweet'), data)
        tweet = Tweet.objects.filter(text='testtext')
        self.assertEqual(tweet.count(),1)


class PostingViewErrorTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@gmail.com', password= 'ttt019283est')

    def test_empty_text(self):
        data = {
          'text': '',
          'author': 'test@gmail.com',
          'created_at': '2022-03-25 17:10:39+09:00',
        }
        self.response = self.client.post(reverse('tweet:tweet'), data)
        self.assertEqual(self.response.status_code, 200)
