from django.db import models
from django.contrib.auth.models import AbstractUser

from .manager import CustomUserManager


class CustomUserModel(AbstractUser):
	username = None
	phone_number = models.CharField(max_length=11, unique=True)
	otp_code = models.PositiveIntegerField(blank=True, null=True)
	otp_code_datetime_created = models.DateTimeField(auto_now=True)

	objects = CustomUserManager()
	backend = 'accounts.backends.PhoneAuthBackend'
	USERNAME_FIELD = 'phone_number'
	REQUIRED_FIELDS = []


