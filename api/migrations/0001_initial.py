# Generated by Django 4.1.5 on 2023-05-26 22:10

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diseases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', help_text='Codigo enfermedad', max_length=20, unique=True, verbose_name='code')),
                ('name', models.CharField(default='', help_text='Nombre enfermedad', max_length=200, verbose_name='Name')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
            ],
            options={
                'verbose_name_plural': 'Enfermedades',
            },
        ),
        migrations.CreateModel(
            name='Professionals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='Nombre profecional', max_length=50, verbose_name='Name')),
                ('last_name', models.CharField(default='', help_text='Apellido del profecional', max_length=50, verbose_name='Last name')),
                ('type_document', models.IntegerField(choices=[(0, 'C.c'), (1, 'C.e')], default=0, help_text='Tipo de documento')),
                ('number_document', models.IntegerField(default=0, help_text='Número de documento', verbose_name='Number Document')),
                ('role', models.IntegerField(choices=[(0, 'Psiquiatr@'), (1, 'Enfermer@'), (9, 'Otro')], default=0, help_text='Rol de profeciona')),
                ('workshift', models.IntegerField(choices=[(0, 'Diruno'), (1, 'Nocturno')], default=0, help_text='Turno de trabajo')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
            ],
            options={
                'verbose_name_plural': 'Profecionales',
            },
        ),
        migrations.CreateModel(
            name='Zones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='Nombre zona', max_length=200, verbose_name='Name')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
            ],
            options={
                'verbose_name_plural': 'Zonas',
            },
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='Nombre paciente', max_length=50, verbose_name='Name')),
                ('last_name', models.CharField(default='', help_text='Apellido del paciente', max_length=50, verbose_name='Last name')),
                ('type_document', models.IntegerField(choices=[(0, 'C.c'), (1, 'T.i'), (2, 'R.c'), (3, 'C.e')], default=0, help_text='Tipo de documento')),
                ('number_document', models.IntegerField(default=0, help_text='Número de documento', verbose_name='Number Document')),
                ('birth_date', models.DateField(help_text='Fecha nacimiento del paciente', verbose_name='Birth date')),
                ('age', models.IntegerField(default=0, help_text='Edad del paciente', verbose_name='Age')),
                ('eps', models.CharField(choices=[('EPS002', 'SALUD TOTAL ENTIDAD PROMOTORA DE SALUD DEL REGIMEN CONTRIBUTIVO Y DEL REGIMEN SUBSIDIADO S.A.'), ('EPS008', 'CAJA DE COMPENSACIÓN FAMILIAR COMPENSAR'), ('EPS041', 'NUEVA EPS S.A. -CM'), ('EPSC34', 'CAPITAL SALUD ENTIDAD PROMOTORA DE SALUD DEL RÉGIMEN SUBSIDIADO SAS "CAPITAL SALUD EPS-S S.A.S." -CM'), ('EPS037', 'NUEVA EPS S.A.'), ('EPS005', 'ENTIDAD PROMOTORA DE SALUD SANITAS S.A.S.'), ('EPS017', 'EPS FAMISANAR S.A.S.'), ('CCFC55', 'CAJACOPI EPS S.A.S -CM'), ('EPSIC6', 'PIJAOS SALUD EPSI -CM'), ('EAS027', 'FONDO PASIVO SOCIAL DE LOS FERROCARRILES NACIONALES'), ('ESSC24', 'COOSALUD EPS S.A. -CM'), ('EPS010', 'EPS SURAMERICANA S.A.'), ('EPS042', 'COOSALUD EPS S.A.'), ('EPS018', 'ENTIDAD PROMOTORA DE SALUD SERVICIO OCCIDENTAL DE SALUD S.A. S.O.S.'), ('EPSIC5', 'ENTIDAD PROMOTORA DE SALUD MALLAMAS EPSI -CM')], default='', help_text='Codigo Eps del paciente', max_length=10, verbose_name='Eps')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('diseases', models.ManyToManyField(help_text='Enfermedades del paciente', to='api.diseases')),
                ('zone', models.ForeignKey(help_text='Zona de ubicación del paciente', on_delete=django.db.models.deletion.PROTECT, to='api.zones')),
            ],
            options={
                'verbose_name_plural': 'Pacientes',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, max_length=254, unique=True, verbose_name='email address')),
                ('phone_number', models.CharField(default='', max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: +999999999. Up to 10 digits allowed.', regex='\\+?1?\\d{9,10}$')], verbose_name='phone')),
                ('is_verified', models.BooleanField(default=True, help_text='Set to true when the user have verified its email address.', verbose_name='verified')),
                ('role', models.IntegerField(choices=[(0, 'Admin')], default=0)),
                ('type_document', models.IntegerField(choices=[(0, 'Cedula Ciudadania')], default=0)),
                ('number_document', models.IntegerField(default=0, verbose_name='Número documento')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
