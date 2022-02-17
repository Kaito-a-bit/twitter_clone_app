from pickle import FALSE
from pyexpat import model
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(_("username"), max_length=24, validators=[username_validator], blank=FALSE)
    email = models.EmailField(_("email"), unique=True)
    is_active = models.BooleanField(_("active"), default=True)
    birthday = models.DateField

    objects = UserManager() #use objects to get the User information from views.py and the like.
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ['username']
