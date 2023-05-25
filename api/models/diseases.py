""""Models DISEASES"""

from django.db import models

class Diseases(models.Model):
    code = models.CharField('code', max_length=20, unique=True, default="", help_text="Codigo enfermedad")
    name = models.CharField('Name', max_length=200, default="", help_text="Nombre enfermedad")

    created_at = models.DateTimeField('created at', auto_now_add=True, help_text='Date time on which the object was created.')
    modified_at = models.DateTimeField('modified at', auto_now=True, help_text='Date time on which the object was last modified.')

    def __str__(self):
        return f"{self.code}: {self.name}"

    class Meta:
        verbose_name_plural = "Enfermedades"