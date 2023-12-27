from django.core import validators
from django.db import models

from my_plants_CBV.web.validators import validate_string_start_with_capital, validate_string_is_only_letters


# Create your models here.


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=(validators.MinLengthValidator(2),),
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=20,
        validators=[validate_string_start_with_capital],
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=20,
        validators=[validate_string_start_with_capital],
        null=False,
        blank=False,
    )


PLANTS_CHOICES = (
    ("outdoor", "Outdoor Plants"),
    ("indoor ", "Indoor  Plants"),
)


class Plant(models.Model):
    type = models.CharField(
        null=False,
        blank=False,
        max_length=14,
        choices=PLANTS_CHOICES,
    )

    name = models.CharField(
        max_length=20,
        validators=(validators.MinLengthValidator(2), validate_string_is_only_letters),
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )