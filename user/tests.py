
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from .models import User

class TopViewTests(TestCase):
  def testStatus(self):
    self.response = self.client.get('/')
    self.assertEqual(self.response.status_code, 200)


class SignUpViewTests(TestCase):
  def testStatus(self):
    self.response = self.client.get('/signup/')
    self.assertEqual(self.response.status_code, 200)

  def test_redirect_to_home(self):
    data = {
      'username': 'Gym Motivation',
      'email': 'karenMotive@gmail.com',
      'birthday': '2002-1-1',
      'password1': 'djdksjk824564',
      'password2': 'djdksjk824564',
    }
    self.response = self.client.post(reverse('user:signup'), data)
    self.assertRedirects(self.response, reverse('user:home'), status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

class HomeViewTests(TestCase):
  def testStatus(self):
    self.response = self.client.get('/home/')
    self.assertEqual(self.response.status_code, 200)
    

class RegisterErrorTests(TestCase):
  def test_too_short_password(self):
    """
    rejects too short password. 
    """
    data = {
      'username': 'peter',
      'email': 'peter@gmail.com',
      'birthday': '1999-1-1',
      'password1': '0sv6d',
      'password2': '0sv6d',
    }
    self.response = self.client.post(reverse('user:signup'), data)
    self.assertEqual(self.response.status_code, 200)

  def test_too_long_username(self):
    """
    rejects username longer than 24 charactors
    """
    data = {
      'username': 'peter01234567890abcdefghijk',
      'email': 'peter@gmail.com',
      'birthday': '1999-1-1',
      'password1': '0sv6d23678',
      'password2': '0sv6d23678',
    }
    self.response = self.client.post(reverse('user:signup'), data)
    self.assertEqual(self.response.status_code, 200)

  def test_not_unique_email(self):
    """
    rejects email which is not enique.
    """
    data = {
      'username': 'erick',
      'email': 'peter123@gmail.com',
      'birthday': '1777-1-1',
      'password1': '0sv6d236781334',
      'password2': '0sv6d236781334',
    }
    self.response = self.client.post('/signup/', data)
    user = User.objects.filter(email='peter123@gmail.com')
    self.assertFalse(user.exists())
    
  def test_wrong_email(self):  
    data = {
      'username': 'erick',
      'email': 'peter123@',
      'birthday': '1999-1-1',
      'password1': '0sv6d23643334',
      'password2': '0sv6d23643334',
    }
    self.response = self.client.post('/signup/', data)
    self.assertEqual(self.response.status_code, 200)

