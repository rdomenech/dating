from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class Interest(models.Model):
    """
    It represents the member's interest.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Member(models.Model):
    """
    It represents the platform's member.
    """

    MALE = 0
    FEMALE = 1

    GENDER_CHOICES = ((MALE, 'Male'), (FEMALE, 'Female'))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.PositiveSmallIntegerField(
        choices=GENDER_CHOICES, default=MALE, validators=[MinValueValidator(0)])
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(0)])
    interests = models.ManyToManyField(Interest)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)

