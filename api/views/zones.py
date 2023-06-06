from django.shortcuts import render, redirect
from django.views import View

from api.models.zones import Zones
from api.models.questions import Questions
from api.models.options import Options
from api.models.Answers import Answers
from api.models.professionals import Professionals
from api.models.patients import Patients

class ZonesView(View):
    zones = Zones.objects.all()
    professionals = Professionals.objects.filter(role=0)
    nurses = Professionals.objects.filter(role=1)

    def get(self, request, zone_id):
        if not request.user.is_authenticated:
            return redirect('api:login')

        zone = Zones.objects.get(id=zone_id)
        return render(
            request,
            template_name='CtlT/zone.html',
            context={
                "zones": self.zones,
                "zone": zone,
                "professionals": self.professionals,
                "nurses": self.nurses
            }
        )
    
    def post(self, request, zone_id):
        if not request.user.is_authenticated:
            return redirect('api:login')

        data = request.POST
        zone = Zones.objects.get(id=zone_id)

        for key in list(data.keys()):
            if 'question' in key.split('_'):
                patient_id = data.get('patient_id')
                patient = Patients.objects.get(id=patient_id)

                professional_id = data.get('professional_id')
                professional = Professionals.objects.get(id=professional_id)

                nurse_id = data.get('nurse_id')
                nurse = Professionals.objects.get(id=nurse_id)

                question_id = key.split('_')[1]
                question = Questions.objects.get(id=question_id)

                answer = Answers(zone=zone, professional=professional, nurse=nurse, patient=patient, question=question,)
                answer.save()

                for option_id in data.getlist('question_{}'.format(question.id)):
                    option = Options.objects.get(id=option_id)
                    answer.selected_option.add(option)
                
        return render(
            request,
            template_name='CtlT/zone.html',
            context={
                "zones": self.zones,
                "zone": zone,
                "professionals": self.professionals,
                "nurses": self.nurses,
                "message": "Saved Successfully"
            }
        )