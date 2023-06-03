# Generated by Django 3.1.14 on 2023-06-02 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20230602_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='zone',
            field=models.ForeignKey(help_text='Zona de ubicación del paciente', on_delete=django.db.models.deletion.PROTECT, related_name='patients', to='api.zones'),
        ),
    ]
