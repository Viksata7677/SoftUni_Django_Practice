from django.db.models import TextChoices


class LanguageChoice(TextChoices):
    PYTHON = 'py', 'Python'
    JAVASCRIPT = 'js', 'JavaScript'
    C = 'c', 'C'
    C_PLUS_PLUS = 'cpp', 'C++'
    OTHER = 'other', 'Other'