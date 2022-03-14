
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
      'password': '0sv6d'
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
      'password': '0sv6d23678'
    }
    self.response = self.client.post(reverse('user:signup'), data)
    self.assertEqual(self.response.status_code, 200)

  def test_too_old_birthday(self):
    """
    rejects user with too old birthday.
    """
    data = {
      'username': 'erick',
      'email': 'peter@gmail.com',
      'birthday': '1777-1-1',
      'password': '0sv6d23678'
    }
    self.response = self.client.post(reverse('user:signup'), data)
    self.assertEqual(self.response.status_code, 200)

    
