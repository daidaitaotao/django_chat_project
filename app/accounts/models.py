# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    FEMALE = 1
    MALE = 2
    UNISEX = 3
    GENDER_CHOICES = (
        (FEMALE, 'female'),
        (MALE, 'male'),
        (UNISEX, 'unisex'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.user.username
