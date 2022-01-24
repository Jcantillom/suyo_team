from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):

    name=models.CharField(max_length=200)
    email = models.EmailField (max_length=200, unique=True)
    password = models.CharField(max_length=200)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self,app_label):
        return True




