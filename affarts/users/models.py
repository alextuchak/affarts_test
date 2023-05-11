from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

USER_TYPE_CHOICES = (
    ('seller', 'Продавец'),
    ('buyer', 'Покупатель'),
)


class CustomUser(BaseUserManager):

    use_in_migrations = True

    def create(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self.create(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have status is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have status is_superuser=True')
        return self.create(email, password, **extra_fields)


class User(AbstractUser):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    object = CustomUser()
    email = models.EmailField(_('email adress'), unique=True)
    first_name = models.CharField(max_length=32, null=True)
    last_name = models.CharField(max_length=32, null=True)
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(max_length=32, unique=False)
    is_active = models.BooleanField(default=True)
    type = models.CharField(verbose_name='Тип пользователя', choices=USER_TYPE_CHOICES, max_length=16, default='buyer')
