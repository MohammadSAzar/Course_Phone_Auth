from django.contrib.auth.backends import ModelBackend

from .models import CustomUserModel

class PhoneAuthBackend(ModelBackend):

	def authenticate(self, request, username=None, password=None, **kwargs):
		phone_number = kwargs['phone_number']
		try:
			user = CustomUserModel.objects.get(phone_number=phone_number)
		except CustomUserModel.DoesNotExist:
			pass
