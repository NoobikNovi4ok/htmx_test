from pathlib import Path
from django.utils.translation import gettext_lazy as _
import environ
import os

env = environ.Env()
environ.Env.read_env()  # Читает .env файл

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    # Mathfilters
    "mathfilters",
    # THUMBNAILS
    # "sorl.thumbnail", # Как в видео
    "easy_thumbnails",
    # Админка
    "admin_interface",
    "colorfield",
    # Стандартные приложения
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # apps
    "shop.apps.ShopConfig",
    "cart.apps.CartConfig",
    "recommend",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # Для локализации
    "django.middleware.locale.LocaleMiddleware",
    #
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "htmx_test.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # Context for categories
                "shop.context_processors.categories",
                # Context for carts
                "cart.context_processors.cart",
            ],
        },
    },
]

WSGI_APPLICATION = "htmx_test.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": env("DB_NAME"),
#         "USER": env("DB_USER"),
#         "PASSWORD": env("DB_PASSWORD"),
#         "HOST": env("DB_HOST"),
#         "PORT": env("DB_PORT"),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Для локализации
LANGUAGE_CODE = "ru"

LANGUAGES = [
    ("en", _("English")),
    ("ru", _("Russian")),
    # добавьте другие языки по мере необходимости
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
]
#

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

STATICFILES_DIRS = [BASE_DIR / "static", "/var/www/static/"]

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

INTERNAL_IPS = [
    "127.0.0.1",
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# AUTH_USER_MODEL = "users.User"

# LOGIN_URL = "/user/login/"
# LOGIN_REDIRECT_URL = "/user/profile"

# Например, вы можете установить размеры миниатюр по умолчанию: ДЛЯ easy-thumbnails
THUMBNAIL_ALIASES = {
    "": {
        "small": {"size": (100, 100), "crop": True},
        "medium": {"size": (300, 300), "crop": True},
        "large": {"size": (600, 600), "crop": True},
    },
}
