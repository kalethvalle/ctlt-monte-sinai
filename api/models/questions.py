"""Model Questions"""
from django.db import models
from api.models.zones import Zones

class Questions(models.Model):
    question = models.CharField('Name', max_length=500, default="", help_text="Pregunta a formular")
    
    zone = models.ForeignKey(Zones, on_delete=models.PROTECT, related_name="questions", help_text="Zona de pregunta a formular")

    created_at = models.DateTimeField('created at', auto_now_add=True, help_text='Date time on which the object was created.')
    modified_at = models.DateTimeField('modified at', auto_now=True, help_text='Date time on which the object was last modified.')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = "Preguntas"
