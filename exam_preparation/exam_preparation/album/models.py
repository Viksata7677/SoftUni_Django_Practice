from django.core.validators import MinValueValidator
from django.db import models

from exam_preparation.profiles.models import Profile


# Create your models here.

class GenreChoices(models.TextChoices):
    POP_MUSIC = "Pop Music", "Pop Music"
    JAZZ_MUSIC = "Jazz Music", "Jazz Music"
    R_AND_B_MUSIC = "R&B Music", "R&B Music"
    ROCK_MUSIC = "Rock Music", "Rock Music"
    COUNTY_MUSIC = "Country Music", "Country Music"
    DANCE_MUSIC = "Dance Music", "Dance Music"
    HIP_HOP_MUSIC = "Hip Hop Music", "Hip Hop Music"
    OTHER = "Other", "Other"


class Album(models.Model):
    album_name = models.CharField(max_length=30, unique=True)
    artist = models.CharField(max_length=30)
    genre = models.CharField(max_length=30, choices=GenreChoices.choices)
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField()
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    owner = models.ForeignKey(to=Profile, on_delete=models.CASCADE)
