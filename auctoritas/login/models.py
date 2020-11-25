import datetime

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, password=None, admin=False):
        if not username:
            raise ValueError("User's must have an username")
        if not password:
            raise ValueError("User's must have an password")
        user = self.model(username = self.get_by_natural_key(username))
        user.set_password(password)
        user = admin
        user.save(using=self._db)
        return user
    def create_employee(self, username, password=None):
        user = self.create_employee(
            username,
            password=password,
            admin =True,
        )
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=200, unique=True, default="", editable=False)
    admin = models.BooleanField(unique=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'username'

    def _str_(self):
        return self.username

    def user_name(self):
        return self.username

    def user_name(self):
        return self.admin

    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True

class User_Info(models.Model):
    password = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.date, blank=True)
    time_in = models.DateTimeField(default=datetime.datetime.now,  blank=True)
    time_out = models.DateTimeField(default=datetime.datetime.now,  blank=True)


    def _str_(self):
        return self.username