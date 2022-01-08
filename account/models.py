from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail

class UserManager(BaseUserManager):
    def _create(self):
        ...
