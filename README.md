Необходимо создать файл в htmx_test ( settings.py ) .env

В нем написать

SECRET_KEY=''

DB_NAME=namedb

DB_USER=postgres

DB_PASSWORD=password

DB_HOST=localhost

DB_PORT=5432

- pip install Django psycopg2 Pillow django-environ
- pip install django-redis
- pip install setuptools(Асинхронно)

Красивые цвета в админке

- pip install django-admin-interface
  Add admin_interface and colorfield to settings.INSTALLED_APPS before django.contrib.admin

INSTALLED_APPS = (
#...
"admin_interface",
"colorfield",
#...
"django.contrib.admin",
#...
)

Run python manage.py migrate

Run python manage.py collectstatic --clear

Restart your application server
