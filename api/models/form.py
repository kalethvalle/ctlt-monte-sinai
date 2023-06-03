"""Model Questions"""
from django.db import models
from api.models.options import Options
from api.models.questions import Questions
from api.models.zones import Zones
class Answer(models.Model):
    usuario = models.CharField(max_length=50, default="")

    zone = models.ForeignKey(Zones, on_delete=models.PROTECT, default=1)
    question = models.ForeignKey(Questions, on_delete=models.PROTECT)
    selected_option = models.ForeignKey(Options, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.usuario} "
    
