from django.contrib import admin
from api.models.users import User
from api.models.zones import Zones
from api.models.diseases import Diseases
from api.models.patients import Patients
from api.models.professionals import Professionals

class Admin(admin.AdminSite):
    site_header = "Control de turno"
    index_title = "Administración clinica  monte sinai"
    site_title = site_header

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'username',
        'first_name',
        'last_name',
        'phone_number',
        'type_document',
        'number_document',
    )

    search_fields  = (
        'email',
        'username',
        'phone_number',
        'number_document',
    )


class ZoneAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created_at',
        'modified_at'
    )

    search_fields = (
        'name',
    )

    list_filter = (
        'name',
    )

class DiseaseAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
    )

    search_fields = (
        'code',
        'name',
    )

    list_filter = (
        'code',
        'name',
    )

class PatientsAdmin(admin.ModelAdmin):
    list_display = (
        '_fullName',
        'number_document',
        'zone',
    )

    list_filter = (
        'zone__name',
        'diseases__code',
    )

    readonly_fields = ["age"]

    fieldsets =  [
        (
            "Datos personales del paciente",
            {
                "fields": [
                    "name", 
                    "last_name",
                    "type_document",
                    "number_document",
                    "birth_date",
                    "age",
                ],
            },
        ),
        (
            "Otros datos del paciente ",
            {
                "fields": [("zone", "diseases", "eps"),],
            },
        ),
    ]

    radio_fields = {
        "type_document": admin.HORIZONTAL,
    }

    autocomplete_fields = [
        "diseases",
    ]

class ProfessionalsAdmin(admin.ModelAdmin):
    list_display = (
        '_fullName',
        'number_document',
        'role',
        'workshift',
    )

    list_filter = (
        'role',
        'workshift',
    )

    fieldsets =  [
        (
            "Datos personales del profecional",
            {
                "fields": [
                    "name", 
                    "last_name",
                    "type_document",
                    "number_document",
                ],
            },
        ),
        (
            "Otros datos del profecional ",
            {
                "fields": [("role", "workshift"),],
            },
        ),
    ]

    radio_fields = {
        "role": admin.HORIZONTAL,
        "workshift": admin.HORIZONTAL
    }


admin_site = Admin(name="CtlT")
admin_site.register(User, UserAdmin)
admin_site.register(Zones, ZoneAdmin)
admin_site.register(Diseases, DiseaseAdmin)
admin_site.register(Patients, PatientsAdmin)
admin_site.register(Professionals, ProfessionalsAdmin)
