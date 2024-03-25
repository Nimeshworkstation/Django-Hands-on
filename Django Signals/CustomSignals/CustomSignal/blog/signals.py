from django.dispatch import Signal,receiver



#creating Signals
notification = Signal(providing_args=["request","user"])



#Receiver Function
@receiver(notification)
def show_notifiation(sender, **kwargs):
	print(sender)
	print(f'{kwargs}')
	print("Notification")
