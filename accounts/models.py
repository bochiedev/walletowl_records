# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    AbstractUser,
    PermissionsMixin,
    BaseUserManager,
    AbstractUser
)
from django.contrib.auth.models import UserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True,max_length=25)
    email = models.EmailField(unique=True,max_length=254 )
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def full_name(self):
        full_name = '%s %s' % (self.last_name.upper(), self.first_name)
        return full_name.strip()
