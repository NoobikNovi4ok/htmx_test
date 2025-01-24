# Необходимые действия для запуска проекта

1. Необходимо создать файл в `htmx_test` ( рядом с файлом `settings.py` ) - `.env` и в нем написать:

```markdown
SECRET_KEY=''

DB_NAME=namedb

DB_USER=postgres

DB_PASSWORD=password

DB_HOST=localhost

DB_PORT=5432
```

2. Необходимые загрузки

- pip install Django psycopg2 Pillow django-environ
- pip install -U djlint #Необходим для форматирования кода в файлах django-html
- pip install django-redis
- pip install setuptools(Асинхронно)

3. Красивая админка Django</b>

- `pip install django-admin-interface`

- Add <b>admin_interface</b> and <b>colorfield</b> to <b>settings.INSTALLED_APPS</b> before <b>django.contrib.admin</b>

```markdown
INSTALLED_APPS = (
#...
"admin_interface",
"colorfield",
#...
"django.contrib.admin",
#...
)
```

- Run `python manage.py migrate`

- Run `python manage.py collectstatic --clear`

- Restart your application server
