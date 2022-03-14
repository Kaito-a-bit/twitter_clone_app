import datetime
from typing_extensions import Self
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from .models import User

class TopViewTests(TestCase):
  def testStatus(self):
    self.response = self.client.get(reverse('/'))
    self.assertEqual(self.response.status_code, 200)


class SignUpViewTests(TestCase):
  def testStatus(self):
    self.response = self.client.get(reverse('/signup/'))
    self.assertEqual(self.response.status_code, 200)

class RegisterErrorTests(TestCase):
  def was_created_with_decent_date(self):
    """
    it returns False when an account is created with unreal date un the past.
    ex: 1777-1-1
    """
    

  def haa_birthday_in_the_future(self):
    """
    it returns False when an account is created in the future.
    """
    

  def has_too_short_password(self):
    """
    reject password shorter than 8 charactors.
    """
  
  def has_too_long_username(self):
    """
    reject username longer than 24 charactors.
    """

  def has_wrong_email(self):
    """
    reject email in the incorrect format.
    """
    