# ctlt-monte-sinai

### Install dependencies
- python -m pip install -r requirements.txt

### Create migrations
#### If the database is empty, perform the following steps
1. python manage.py makemigrations
2. python manage.py migrate

### Create collectstatic
- python manage.py collectstatic
 
### Run sever
- python manage.py runserver

### Build to .exe
- pyinstaller --clean build.spec

### Distruted
- File `.exe` distributed any user machine
- execute `./file_name.exe runserver localhost:8000 --noreload`