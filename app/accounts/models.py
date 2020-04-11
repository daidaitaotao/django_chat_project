# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from accounts.constants import GENDER_CHOICES


class UserProfile(models.Model):
    """
        user profile to track user data
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.user.username
