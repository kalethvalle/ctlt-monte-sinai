"""Model Questions"""
from django.db import models
from api.models.questions import Questions

class Options(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.PROTECT, help_text="pregunta", related_name="options")
    value = models.CharField('Name', max_length=200, default="", help_text="Opción de pregunta")

    created_at = models.DateTimeField('created at', auto_now_add=True, help_text='Date time on which the object was created.')
    modified_at = models.DateTimeField('modified at', auto_now=True, help_text='Date time on which the object was last modified.')

    def __str__(self):
        return self.value
    
    class Meta:
        verbose_name_plural = "Opciones"
