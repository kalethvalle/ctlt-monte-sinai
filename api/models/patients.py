""""Models PATIENTS"""

from django.db import models
from api.models.zones import Zones
from api.models.diseases import Diseases

class Patients(models.Model):
    zone = models.ForeignKey(Zones, on_delete=models.PROTECT)

    name = models.CharField('Name', max_length=50, default="", help_text="Nombre paciente")
    last_name = models.CharField('Last name', max_length=50, default="", help_text="Apellido del paciente")

    TYPE_DOCUMENT_CHOICES = [(0, 'C.c'), (1, 'T.i'), (2, 'R.c'), (3, 'C.e')]
    type_document = models.IntegerField(choices=TYPE_DOCUMENT_CHOICES, default=0)

    number_document = models.IntegerField('Number Document', default=0, help_text="Número de documento")
    birth_date = models.DateField('Birth date', help_text="Fecha nacimiento del paciente")
    age = models.IntegerField('Age', default=0, help_text="Edad del paciente")

    eps = models.CharField('Eps', max_length=10, default="", help_text="Codigo Eps del paciente")

    diseases = models.ManyToManyField(Diseases)

    created_at = models.DateTimeField('created at', auto_now_add=True, help_text='Date time on which the object was created.')
    modified_at = models.DateTimeField('modified at', auto_now=True, help_text='Date time on which the object was last modified.')

    @property
    def _fullName(self):
        return f"{self.name.capitalize()} {self.last_name.capitalize()}"
    
    def __str__(self):
        return self._fullName
    
    def save(self, *args, **kwargs):
        from datetime import date

        today = date.today()
        self.age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        super(Patients, self).save()
    
    class Meta:
        verbose_name_plural = "Pacientes"
