from django.http import JsonResponse
from django.views import View
import json

from api.models.patients import Patients

class PatientsView(View):
    def get(self, request, patient_id):
        if request.user.is_authenticated:
            diseases = []
            patient = Patients.objects.get(id=patient_id)

            for disease in patient.diseases.all():
                diseases.append(disease.code)

            return JsonResponse({"document": patient.number_document, "eps": patient.eps, "diseases": diseases}, safe=False)