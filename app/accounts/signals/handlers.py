from django.dispatch import receiver
from django.db.models.signals import post_save
from accounts.models import UserProfile
from django.contrib.auth.models import User


@receiver([post_save], sender=User)
def user_post_create_handler(sender, instance, created, **kwargs):
    """
    """
    if kwargs['raw']:
        return

    if created:
        UserProfile.objects.create(user=instance)
