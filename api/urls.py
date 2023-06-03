from django.urls import path
from api.views.home import HomeView
from api.views.zones import ZonesView

app_name = 'api'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path("zone/<int:zone_id>/", ZonesView.as_view(), name="zone"),
]