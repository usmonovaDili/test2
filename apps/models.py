import datetime

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractUser


class ToDoUser(BaseUserManager):
    def create_user(self, email, username, age, password=None, **extra_fields):
        if not email:
            raise ValueError('email kiritishingiz shart')
        if not username:
            raise ValueError('"username" kiriting')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            age=age,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, name, age, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            name=name,
            age=age,
            password=password
        )


class TODO(AbstractBaseUser):
    STAFF_CHOICES = (
        (False, 'admin'),
        (True, 'user')
    )

    email = models.EmailField(verbose_name='email', max_length=50, unique=True)
    username = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='data join')
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=True)
    is_staff = models.BooleanField(choices=STAFF_CHOICES, default=False)
    name = models.CharField(max_length=50)
    age = models.DateField(default=datetime.date.today())
    status = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name', 'age']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
