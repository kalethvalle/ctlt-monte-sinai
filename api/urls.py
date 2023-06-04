from django.urls import path
from api.views.login import LoginView
from api.views.logout import LogoutView
from api.views.home import HomeView
from api.views.zones import ZonesView
from api.views.patients import PatientsView

app_name = 'api'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('zone/<int:zone_id>/', ZonesView.as_view(), name='zone'),
    path('patient/<int:patient_id>', PatientsView.as_view(), name='patient'),
]