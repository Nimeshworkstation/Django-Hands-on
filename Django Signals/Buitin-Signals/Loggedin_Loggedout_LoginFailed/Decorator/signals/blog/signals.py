from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User 
from django.dispatch import receiver

@receiver(user_logged_in,sender=User)
def login_success(sender, request, user, **kwargs):
	print("---------------------------")
	print("Logged in Signal... Run Intro..")
	print("Sender:" , sender)
	print("Request:", request)
	print("User: ", user)
	print(f'Kwargs: {kwargs}')

@receiver(user_logged_out,sender=User)
def log_out(sender, request, user, **kwargs):
	print("---------------------------")
	print("Logged out Signal... Run Bye Bye...")
	print("Sender:" , sender)
	print("Request:", request)
	print("User: ", user)
	print(f'Kwargs: {kwargs}')

@receiver(user_login_failed)
def login_failed(sender, request, credentials, **kwargs):
	print("---------------------------")
	print("Login Failed Signal... Run  Failed...")
	print("Sender:" , sender)
	print("Credentials:" , credentials)
	print("Request:", request)
	print(f'Kwargs: {kwargs}')


