from PyInstaller.utils.hooks import collect_data_files, collect_submodules
import os

static_dir = os.path.join(os.getcwd(), "static")
template_dir = os.path.join(os.getcwd(), "api", "templates")
db_file = os.path.join(os.getcwd(), "db.sqlite3")
block_cipher = None  # Asegúrate de definir esto si no lo usas

# Configuración de Analysis
a = Analysis(
    ['manage.py'],  # Punto de entrada
    pathex=["."],  # Usar ruta absoluta del proyecto
    binaries=[],
    datas=[ 
        (static_dir, "static"),  # Archivos estáticos
        (template_dir, "templates"),  # Templates
        (db_file, "."),  # Base de datos
        # (os.path.join(os.getcwd(), "api"), "api"),
        *collect_data_files("django"),
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
    # onefile=True,
)