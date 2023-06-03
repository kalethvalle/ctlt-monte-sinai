from django.shortcuts import render, redirect
from django.views import View

from api.models.zones import Zones

class HomeView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('api:login')

        zones = Zones.objects.all()
        return render(
            request,
            template_name='CtlT/home.html',
            context={
                "zones": zones
            }
        )
