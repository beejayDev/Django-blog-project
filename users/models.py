from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
#from django.conf import settings 
from django.contrib.auth import get_user_model

class AccountUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, username, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        #if not email:
            #raise ValueError('The given email must be set')
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, username, **extra_fields)

    def create_superuser(self, email, username, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, username, password, **extra_fields)


class AccountUser(AbstractUser):
    #username = None
    email = models.EmailField(_('email address'), unique=True)

    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = AccountUserManager()


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} Profile"



