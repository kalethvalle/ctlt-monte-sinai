"""Models PROFESSIONALS"""

from django.db import models

class Professionals(models.Model):
    name = models.CharField('Name', max_length=50, default="", help_text="Nombre profecional")
    last_name = models.CharField('Last name', max_length=50, default="", help_text="Apellido del profecional")

    TYPE_DOCUMENT_CHOICES = [(0, 'C.c'), (1, 'C.e')]
    type_document = models.IntegerField(choices=TYPE_DOCUMENT_CHOICES, default=0, help_text="Tipo de documento")

    number_document = models.IntegerField('Number Document', default=0, help_text="Número de documento")

    ROLE_CHOICES = [(0, 'Psiquiatr@'), (1, 'Enfermer@'), (9, 'Otro')]
    role = models.IntegerField(choices=ROLE_CHOICES, default=0, help_text="Rol de profeciona")

    WORKSHIFT_CHOICES = [(0, 'Diruno'), (1, 'Nocturno')]
    workshift = models.IntegerField(choices=WORKSHIFT_CHOICES, default=0, help_text="Turno de trabajo")

    created_at = models.DateTimeField('created at', auto_now_add=True, help_text='Date time on which the object was created.')
    modified_at = models.DateTimeField('modified at', auto_now=True, help_text='Date time on which the object was last modified.')

    @property
    def _fullName(self):
        return f"{self.name.capitalize()} {self.last_name.capitalize()}"

    def __str__(self):
        return self._fullName

    class Meta:
        verbose_name_plural = "Profecionales"