""""Models ZONE"""

from django.db import models

class Zones(models.Model):
    name = models.CharField('Name', max_length=200, default="", help_text="Nombre zona")

    created_at = models.DateTimeField('created at', auto_now_add=True, help_text='Date time on which the object was created.')
    modified_at = models.DateTimeField('modified at', auto_now=True, help_text='Date time on which the object was last modified.')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Zonas"