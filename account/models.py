from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from .utils import generate_activation_code


class UserManager(BaseUserManager):
    def _create(self, email, password, name, **extra_fields):
        if not email:
            raise ValueError('please, enter your email')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        print(password)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, name, **extra_fields):
        # activation_code = generate_activation_code()
        # extra_fields.setdefault('activation_code', str(activation_code))
        extra_fields.setdefault('is_active', 'False')
        extra_fields.setdefault('is_staff', 'False')
        return self._create(email, password, name, **extra_fields)

    def create_superuser(self, email, password, name, **extra_fields):
        extra_fields.setdefault('is_active', 'True')
        extra_fields.setdefault('is_staff', 'True')
        return self._create(email, password, name, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=70)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=50, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, obj=None):
        return self.is_staff

    # def send_activation_email(self, action):
    #     # action can be account activation a passwordr restoration
    #     if action.lower() == 'register':
    #         subject = 'Account activation'
    #         ''' CHECk ThIS ACTIVATION URL'''
    #         message = f'Follow this link to finalize your registration:\nhttp://localhost:8000/account/activate/{self.activation_code}/'
    #     else:
    #         subject = 'Password change'
    #         # this is not the final version of the message
    #         # message = f'This is your confirmation code: {self.activation_code}'

    #     send_mail(
    #         subject,
    #         message,
    #         'shop_staff@gmail.com',
    #         self.email
    #     )