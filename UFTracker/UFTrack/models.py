from django.db import models
from django.core.validators import MinValueValidator


class UF(models.Model):
    value = models.FloatField(validators=[MinValueValidator(0.0)])
    date = models.DateField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.date} {self.value}'
