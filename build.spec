from PyInstaller.utils.hooks import collect_data_files, collect_submodules
import os

staticfiles_dir = os.path.join(os.getcwd(), 'staticfiles')
static_dir = os.path.join(os.getcwd(), 'static') 
template_dir = os.path.join(os.getcwd(), "api", "templates")
db_file = os.path.join(os.getcwd(), "db.sqlite3")
admin_static_dir = os.path.join(os.getcwd(), "staticfiles", "admin")
wsgi_file = os.path.join(os.getcwd(), 'ctl_turno', 'wsgi.py')
block_cipher = None

# Configuración de Analysis
a = Analysis(
    ['manage.py'],  # Punto de entrada
    pathex=[os.getcwd()],  # Usar ruta absoluta del proyecto
    binaries=[],
    datas=[ 
        (staticfiles_dir, 'staticfiles'),
        (static_dir, 'static'),
        (template_dir, "templates"),
        (admin_static_dir, 'static/admin'),
        (wsgi_file, 'ctl_turno'),
        (db_file, "."),
        *collect_data_files("django"),
        *collect_data_files("whitenoise"),
    ],
    hiddenimports=[ 
        *collect_submodules("django"),
        *collect_submodules("api"),
        "django.core.handlers.wsgi",
        "django.core.management",
        "django.utils",
        "asgiref",  # Dependencia requerida
        "sqlparse",  # Dependencia para la consola de Django
        "dns.rdtypes.*",
        "dns.rdtypes.ANY.*",
        "django.contrib",
        "django.contrib.admin.apps",
        "django.contrib.auth.apps",
        "django.contrib.contenttypes.apps",
        "django.contrib.sessions.models",
        "django.contrib.sessions.apps",
        "django.contrib.messages.middleware",
        "django.contrib.auth.middleware",
        "django.contrib.sessions.middleware",
        "django.contrib.sessions.serializers",
        "whitenoise",
        "whitenoise.storage",
        "whitenoise.middleware",
        "whitenoise.runserver_nostatic",
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_rediects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='ludo_tech',
    debug=False,
    console=True,
)