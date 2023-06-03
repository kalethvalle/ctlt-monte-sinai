from django.shortcuts import render, redirect
from django.views import View

from api.models.zones import Zones
from api.models.questions import Questions
from api.models.options import Options
from api.models.form import Answer

class ZonesView(View):
    def get(self, request, zone_id):
        if not request.user.is_authenticated:
            return redirect('api:login')

        zones = Zones.objects.all()
        zone = Zones.objects.get(id=zone_id)
        return render(
            request,
            template_name='CtlT/zone.html',
            context={
                "zones": zones,
                "zone": zone
            }
        )
    
    def post(self, request, zone_id):
        data = request.POST
        zone = Zones.objects.get(id=zone_id)

        for key in list(data.keys()):
            if 'question' in key.split('_'):
                question_id = key.split('_')[1]
                question = Questions.objects.get(id=question_id)

                option_id = data.get('question_{}'.format(question.id))
                option = Options.objects.get(id=option_id)
                Answer.objects.create(
                    usuario=data.get('usuario'),
                    zone=zone,
                    question=question,
                    selected_option=option
                )
        
        zones = Zones.objects.all()
        

        return render(
            request,
            template_name='CtlT/zone.html',
            context={
                "zones": zones,
                "zone": zone,
                "message": "Saved Successfully"
            }
        )