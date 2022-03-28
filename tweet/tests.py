from django.test import TestCase
from django.urls import reverse
from .models import Tweet
from user.models import User

class PostingViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@gmail.com', password='ttt019283est')
        self.client.login(username="test@gmail.com", password="ttt019283est")

    def test_post_success(self):
        data = {
          'text': 'testtext',
        }
        self.response = self.client.post(reverse('tweet:tweet'), data)
        self.assertRedirects(self.response, reverse('user:home'))

    def test_get_success(self):
        self.response = self.client.get(reverse('tweet:tweet'))
        self.assertEqual(self.response.status_code, 200)    
    
    def test_tweet_creation(self):
        data = {
          'text': 'testtext',
        }
        self.response = self.client.post(reverse('tweet:tweet'), data)
        tweet = Tweet.objects.filter(text='testtext')
        self.assertEqual(tweet.count(),1)


class PostingViewErrorTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@gmail.com', password='ttt019283est')
        self.client.login(username="test@gmail.com", password="ttt019283est")

    def test_empty_text(self):
        data = {
          'text': '',
        }
        self.response = self.client.post(reverse('tweet:tweet'), data)
        self.assertEqual(self.response.status_code, 200)
        tweet = Tweet.objects.filter(author=self.user) 
        self.assertEqual(tweet.count(),0)
