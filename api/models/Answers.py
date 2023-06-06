"""Model Questions"""
from django.db import models
from api.models.zones import Zones
from api.models.patients import Patients
from api.models.professionals import Professionals
from api.models.questions import Questions
from api.models.options import Options

class Answers(models.Model):
    zone = models.ForeignKey(Zones, on_delete=models.PROTECT, related_name='zones')
    professional = models.ForeignKey(Professionals, on_delete=models.PROTECT, related_name='professional')
    nurse = models.ForeignKey(Professionals, on_delete=models.PROTECT, related_name='nurses')
    patient = models.ForeignKey(Patients, on_delete=models.PROTECT, related_name='patients')
    question = models.ForeignKey(Questions, on_delete=models.PROTECT, related_name='questions')
    selected_option = models.ManyToManyField(Options, related_name='options')

    created_at = models.DateTimeField('created at', auto_now_add=True, help_text='Date time on which the object was created.')
    modified_at = models.DateTimeField('modified at', auto_now=True, help_text='Date time on which the object was last modified.')

    def __str__(self):
        return f"Formulario {self.zone.name} - {self.patient._fullName}"
    
    class Meta:
        verbose_name_plural = "Respuestas"
    
