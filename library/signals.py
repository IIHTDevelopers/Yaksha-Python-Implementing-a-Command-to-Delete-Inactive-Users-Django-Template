import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Setting up a logger for user registration
logger = logging.getLogger(__name__)

@receiver(post_save, sender=User)
def log_user_registration(sender, instance, created, **kwargs):
    """Log user registration details after a user is created."""
    if created:  # Trigger only for new user creation
        username = instance.username
        email = instance.email
        registration_time = instance.date_joined
        # Log the registration details to a file
        logger.info(f"User Registered: {username}, Email: {email}, Registered at: {registration_time}")
