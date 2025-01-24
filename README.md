# Необходимые действия для запуска проекта

1. Для того чтобы начать работу нужно создать файл в `htmx_test` ( рядом с файлом `settings.py` ) - `.env` и в нем написать:

```markdown
SECRET_KEY=''
DB_NAME=namedb
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
```

2. Загрузки

- pip install Django psycopg2 Pillow django-environ
- pip install -U djlint. Необходим для форматирования кода в файлах django-html
- pip install sorl-thumbnail. Для изображений
- pip install django-redis
- pip install setuptools(Асинхронно)

3. Красивая админка Django</b>

- Написать в консоль команду `pip install django-admin-interface`

- Добавить _admin_interface_ и _colorfield_ в _settings.INSTALLED_APPS_ до _django.contrib.admin_

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

- Ввести в терминал `python manage.py migrate`

- Ввести в терминал `python manage.py collectstatic`.

- На свой страх и риск можете добавить `--clear` в конце.( Это удалит все файлы статики, прежде чем сохранит все в одной папке ).

- Можно перезапустить сервер

## Используемые технологии в ходе разработки

- DJANGO
- HTML
- HTMX
- CSS
- JavaScript
- AJAX
- POSTGRESQL
