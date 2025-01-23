Необходимо создать файл в htmx_test ( settings.py ) .env

В нем написать

SECRET_KEY=''

DB_NAME=namedb

DB_USER=postgres

DB_PASSWORD=password

DB_HOST=localhost

DB_PORT=5432

<b>Необходимые загрузки</b>

- pip install Django psycopg2 Pillow django-environ
- pip install -U djlint #Необходим для форматирования кода в файлах django-html
- pip install django-redis
- pip install setuptools(Асинхронно)

<b>Красивые цвета в админке</b>

- <b>pip install django-admin-interface</b>

- Add <b>admin_interface</b> and <b>colorfield</b> to <b>settings.INSTALLED_APPS</b> before <b>django.contrib.admin</b>

  INSTALLED_APPS = (

  #...

  "admin_interface",

  "colorfield",

  #...

  "django.contrib.admin",

  #...

  )

  - Run <b>python manage.py migrate</b>

  - Run <b>python manage.py collectstatic --clear</b>

  - Restart your application server
