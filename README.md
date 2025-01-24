# Проект django-htmx

## Необходимые действия для запуска проекта

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
- pip install ~sorl-thumbnail~. Для изображений из видео
- pip install easy-thumbnails. Использую для изображений, так как тут можно использовать _THUMBNAIL_ALIASES_
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

- Можно также добавить опцию `--clear` в конце:

  - Опция --clear указывает Django сначала удалить все файлы в директории STATIC_ROOT, прежде чем собирать новые статические файлы;
  - Использование --clear поможет избежать путаницы с устаревшими файлами, которые могут остаться в STATIC_ROOT.

- Можно перезапустить сервер

## Используемые технологии в ходе разработки

- DJANGO
- HTML
- HTMX
- CSS
- JavaScript
- AJAX
- POSTGRESQL
- ~SQLITE~

## Мои расширения в VSCODE

### Важные

1. Black Formatter
   - Id: ms-python.black-formatter
   - Description: Formatting support for Python files using the Black formatter.
   - Publisher: Microsoft
2. Django
   - Id: batisteo.vscode-django
   - Description: Beautiful syntax and scoped snippets for perfectionists with deadlines
   - Publisher: Baptiste Darthenay
3. djLint
   - Id: monosans.djlint
   - Description: HTML template formatter and linter (Django, Jinja, Nunjucks, Twig, Handlebars, Mustache)
   - Publisher: monosans
4. Prettier - Code formatter
   - Id: esbenp.prettier-vscode
   - Description: Code formatter using prettier
   - Publisher: Prettier
5. Pylance
   - Id: ms-python.vscode-pylance
   - Description: A performant, feature-rich language server for Python in VS Code
   - Publisher: Microsoft
6. Pylint
   - Id: ms-python.pylint
   - Description: Linting support for Python files using Pylint.
   - Publisher: Microsoft
7. Python
   - Id: ms-python.python
   - Description: Python language support with extension access points for IntelliSense (Pylance), Debugging (Python Debugger), linting, formatting, refactoring, unit tests, and more.
   - Publisher: Microsoft
8. Python Debugger
   - Id: ms-python.debugpy
   - Description: Python Debugger extension using debugpy.
   - Publisher: Microsoft

### Декорации

1. Auto Rename Tag
   - Id: formulahendry.auto-rename-tag
   - Description: Auto rename paired HTML/XML tag
   - Publisher: Jun Han
2. Code Spell Checker
   - Id: streetsidesoftware.code-spell-checker
   - Description: Spelling checker for source code
   - Publisher: Street Side Software
3. CSS Peek
   - Id: pranaygp.vscode-css-peek
   - Description: Allow peeking to css ID and class strings as definitions from html files to respective CSS. Allows peek and goto definition.
   - Publisher: Pranay Prakash
4. GitHub Theme
   - Id: GitHub.github-vscode-theme
   - Description: GitHub theme for VS Code
   - Publisher: GitHub
   - Использую GitHub Dark
5. GitLens — Git supercharged
   - Id: eamodio.gitlens
   - Description: Supercharge Git within VS Code — Visualize code authorship at a glance via Git blame annotations and CodeLens, seamlessly navigate and explore Git repositories, gain valuable insights via rich visualizations and powerful comparison commands, and so much more
   - Publisher: GitKraken
6. HTML CSS Support
   - Id: ecmel.vscode-html-css
   - Description: CSS Intellisense for HTML
   - Publisher: ecmel
7. IntelliSense for CSS class names in HTML
   - Id: Zignd.html-css-class-completion
   - Description: CSS class name completion for the HTML class attribute based on the definitions found in your workspace.
   - Publisher: Zignd
8. Live Sass Compiler
   - Id: glenn2223.live-sass
   - Description: Compile Sass or Scss to CSS at realtime.
   - Publisher: Glenn Marks
9. Live Server
   - Id: ritwickdey.LiveServer
   - Description: Launch a development local Server with live reload feature for static & dynamic pages
   - Publisher: Ritwick Dey
10. markdownlint
    - Id: DavidAnson.vscode-markdownlint
    - Description: Markdown linting and style checking for Visual Studio Code
    - Publisher: David Anson
11. Material Icon Theme
    - Id: PKief.material-icon-theme
    - Description: Material Design Icons for Visual Studio Code
    - Publisher: Philipp Kief
12. Russian - Code Spell Checker
    - Id: streetsidesoftware.code-spell-checker-russian
    - Description: Russian dictionary extension for VS Code.
    - Publisher: Street Side Software
13. SQLite3 Editor
    - Id: yy0931.vscode-sqlite3-editor
    - Description: Edit SQLite3 files like you would in spreadsheet applications.
    - Publisher: yy0931
14. Tabnine: AI Chat & Autocomplete for JavaScript, Python, Typescript, Java, PHP, Go, and more
    - Id: TabNine.tabnine-vscode
    - Description: Tabnine is the AI code assistant that accelerates and simplifies software development while keeping your code private, secure, and compliant. It provides accurate, highly personalized results for generating code, writing unit tests, creating documentation, explaining legacy code, fixing code, and mu
    - Publisher: TabNine
