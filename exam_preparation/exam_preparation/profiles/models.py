from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from exam_preparation.profiles.validators import UsernameValidator


# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=15, validators=[MinLengthValidator(2), UsernameValidator()])
    email = models.EmailField()
    age = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
