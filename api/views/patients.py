from django.http import JsonResponse
from django.views import View
import json

from api.models.patients import Patients

class PatientsView(View):
    def get(self, request, patient_id):
        print('ingreso aqui >>>>')
        if request.user.is_authenticated:
            patient = Patients.objects.get(id=patient_id)
            return JsonResponse({"document": patient.number_document, "eps": patient.eps, }, safe=False)