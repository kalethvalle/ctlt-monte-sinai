# Generated by Django 3.1.14 on 2023-06-02 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_answer_student_name_answer_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='diseases',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='options',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='patients',
            name='eps',
            field=models.CharField(choices=[('EPS002', 'SALUD TOTAL ENTIDAD PROMOTORA DE SALUD DEL REGIMEN CONTRIBUTIVO Y DEL REGIMEN SUBSIDIADO S.A.'), ('EPS008', 'CAJA DE COMPENSACIÓN FAMILIAR COMPENSAR'), ('EPS005', 'ENTIDAD PROMOTORA DE SALUD SANITAS S.A.S.'), ('EPS017', 'EPS FAMISANAR S.A.S.'), ('EPS037', 'NUEVA EPS S.A.'), ('EPSC34', 'CAPITAL SALUD ENTIDAD PROMOTORA DE SALUD DEL RÉGIMEN SUBSIDIADO SAS "CAPITAL SALUD EPS-S S.A.S." -CM'), ('EPSIC6', 'PIJAOS SALUD EPSI -CM'), ('EPS041', 'NUEVA EPS S.A. -CM'), ('CCFC55', 'CAJACOPI EPS S.A.S -CM'), ('EPS042', 'COOSALUD EPS S.A.'), ('EPS010', 'EPS SURAMERICANA S.A.'), ('ESSC24', 'COOSALUD EPS S.A. -CM'), ('EAS027', 'FONDO PASIVO SOCIAL DE LOS FERROCARRILES NACIONALES')], default='', help_text='Codigo Eps del paciente', max_length=10, verbose_name='Eps'),
        ),
        migrations.AlterField(
            model_name='patients',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='professionals',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='zone',
            field=models.ForeignKey(help_text='Zona de pregunta a formular', on_delete=django.db.models.deletion.PROTECT, related_name='questions', to='api.zones'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='zones',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]