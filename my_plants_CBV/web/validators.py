from django.core.exceptions import ValidationError


def validate_string_start_with_capital(value):
    if not value[0] == value[0].capital() or not value[0].isalpha():
        raise ValidationError("Your name must start with a capital letter!")


def validate_string_is_only_letters(value):
    if not value.isalpha():
        raise ValidationError("Plant name should contain only letters!")