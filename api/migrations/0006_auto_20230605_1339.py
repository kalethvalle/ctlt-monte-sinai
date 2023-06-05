# Generated by Django 3.1.14 on 2023-06-05 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20230602_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='diseases',
            field=models.ManyToManyField(help_text='Enfermedades del paciente', related_name='diseases', to='api.Diseases'),
        ),
    ]
