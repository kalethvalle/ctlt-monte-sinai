from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from api.models.zones import Zones

class HomeView(View):
    def get(self, request):
        zones = Zones.objects.all()
        return render(
            request,
            template_name='CtlT/home.html',
            context={
                "zones": zones
            }
        )
