
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields): 
        if not email:
          raise ValueError('ユーザ登録にはEmailアドレスの設定が必要になります')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password) 
        user.save(using=self.db) 
        return user 

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _("username"),
        max_length=24, 
        validators=[username_validator], 
        error_messages =  { "blank": "このフィールドの入力は必須です" }
        )

    email = models.EmailField(
        _("email"),
        unique=True, #これ必須
        error_messages =  { "blank": "このフィールドの入力は必須です",
                            "unique": "あなたが入力したメールアドレスは既に使用されています。" }   
        )

    birthday = models.DateField(
        null=True,
        blank=True,
        )

    is_active = models.BooleanField(_("active"), default=True)
    is_staff = models.BooleanField(_("is_staff"), default=False)

    objects = UserManager() #use objects to get the User information from views.py and the like.
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ['username']

class ConnectionModel(models.Model):
    follower = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    date_creagted = models.DateTimeField(auto_now_add=True)
