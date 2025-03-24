from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from .utils import create_notification

@receiver(user_logged_in)
def login_notification(sender, request, user, **kwargs):
    create_notification(user, "You have logged in successfully.")

@receiver(user_logged_out)
def logout_notification(sender, request, user, **kwargs):
    if user:  # Check if user exists
        create_notification(user, "You have logged out successfully.")
