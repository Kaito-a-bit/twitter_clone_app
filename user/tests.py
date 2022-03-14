
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

class RegisterErrorTests(TestCase):
  def has_too_short_password(self):
    """
    reject password shorter than 8 charactors.
    """
    self.response = self.client.post('/signup/', {
      'username': 'peter',
      'email': 'peter0303@gmail.com',
      'birthday': '199-1-1', 
      'password': '0sv6d'})
    self.assertEqual(self.response.status_code, 200)
  
      
  # def has_too_long_username(self):
  #   """
  #   reject username longer than 24 charactors.
  #   """
  
  # def has_wrong_email(self):
  #   """
  #   reject email in the incorrect format.
  #   """
  
    