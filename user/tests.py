
from django.test import TestCase
from django.urls import reverse
from .models import User

class TopViewTests(TestCase):
    def test_get_success(self):
        self.response = self.client.get(reverse('user:top'))
        self.assertEqual(self.response.status_code, 200)


class SignUpViewTests(TestCase):
    def test_get_success(self):
        self.response = self.client.get(reverse('user:signup'))
        self.assertEqual(self.response.status_code, 200)

    def test_redirect_to_home(self):
        data = {
          'username': 'GymMotivation3',
          'email': 'nanaMotive@gmail.com',
          'birthday': '2002-1-1',
          'password1': 'kjhd1245',
          'password2': 'kjhd1245',
        }
        self.response = self.client.post(reverse('user:signup'), data)
        self.assertRedirects(self.response, '/home/')

class HomeViewTests(TestCase):
    def setUp(self):
        self.user = User.objects._create_user('testuser', 'test@gmail.com', 'ttt019283est')

    def test_get_home_redirect_to_signup(self):
        self.response = self.client.get(reverse('user:home'))
        self.assertRedirects(self.response, '/accounts/login/?next=/home/')

    def test_get_home_success(self):
        self.client.login(email='test@gmail.com', password='ttt019283est')
        self.response = self.client.get(reverse('user:home'))
        self.assertEqual(self.response.status_code, 200)


class SignUpViewErrorTests(TestCase):
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
        user = User.objects.filter(password='0sv6d')
        self.assertEqual(user.count(), 0)
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
        user = User.objects.filter(username='peter01234567890abcdefghijk')
        self.assertEqual(user.count(), 0)
        self.assertEqual(self.response.status_code, 200)

    def test_user_creation(self):
        """
        rejects email which is not enique.
        """
        data = {
          'username': 'erick',
          'email': 'peter1233445@gmail.com',
          'birthday': '1777-1-1',
          'password1': '0sv6d236781334',
          'password2': '0sv6d236781334',
        }
        self.response = self.client.post(reverse('user:signup'), data)
        user = User.objects.filter(email='peter1233445@gmail.com')
        self.assertEqual(user.count(), 1)
        
    def test_wrong_email(self):  
        data = {
          'username': 'erick',
          'email': 'peter123@',
          'birthday': '1999-1-1',
          'password1': '0sv6d23643334',
          'password2': '0sv6d23643334',
        }
        self.response = self.client.post(reverse('user:signup'), data)
        user = User.objects.filter(email='peter123@')
        self.assertEqual(user.count(), 0)
        self.assertEqual(self.response.status_code, 200)


class LogInTests(TestCase):
    def setUp(self):
        self.user = User.objects._create_user('testuser', 'test@gmail.com', 'ttt019283est')

    def test_get_home_redirect_to_signup(self):
        self.response = self.client.get(reverse('user:home'))
        self.assertRedirects(self.response, '/accounts/login/?next=/home/')

    def test_get_home_success(self):
        self.client.login(email='test@gmail.com', password='ttt019283est')
        self.response = self.client.get(reverse('user:home'))
        self.assertEqual(self.response.status_code, 200)


class LogInErrorTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@gmail.com', password= 'ttt019283est')

    def test_wrong_credentials(self):
        self.response = self.client.login(email='test11@gmail.com', password='ttt019283est')
        self.assertEqual(self.response, False)

    def test_empty_credentials(self):
        self.response = self.client.login(email='', password='')
        self.assertEqual(self.response, False)


class LogOutTests(TestCase):
  def setUp(self):
      self.user = User.objects._create_user('testuser', 'test@gmail.com', 'ttt019283est')
    
  def test_get_success(self):
      self.response = self.client.get(reverse('logout'))
      self.assertRedirects(self.response, '/')

