"""
Django settings for web_project project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os, environ
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Application definition
DJANGO_APPS = [
    "material",
    "material.admin",
    # "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core",
    "userapp",
    "boardapp",
    "questionapp",
    "infoapp",
    "screenapp",
    "productapp",
]

PART_APPS = [
    "bootstrap4",
    "ckeditor",
    "ckeditor_uploader",
]


INSTALLED_APPS = DJANGO_APPS + PART_APPS

CKEDITOR_UPLOAD_PATH = "media/"
CKEDITOR_IMAGE_BACKEND = "pillow"


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

MATERIAL_ADMIN_SITE = {
    "HEADER": _("4LEAF SYSTEM - Admin Management System"),  # Admin site header
    "TITLE": _("ADMINSTRATOR"),  # Admin site title
    # "FAVICON": "path/to/favicon",  # Admin site favicon (path to static should be specified)
    "MAIN_BG_COLOR": "#636e72",  # Admin site main color, css color should be specified
    "MAIN_HOVER_COLOR": "#2d3436",  # Admin site main hover color, css color should be specified
    # "PROFILE_PICTURE": "path/to/image",  # Admin site profile picture (path to static should be specified)
    # "PROFILE_BG": "path/to/image",  # Admin site profile background (path to static should be specified)
    # "LOGIN_LOGO": "path/to/image",  # Admin site logo on login page (path to static should be specified)
    # "LOGOUT_BG": "path/to/image",  # Admin site background on login/logout pages (path to static should be specified)
    # "SHOW_THEMES": True,  #  Show default admin themes button
    # "TRAY_REVERSE": True,  # Hide object-tools and additional-submit-line by default
    # "NAVBAR_REVERSE": True,  # Hide side navbar by default
    # "SHOW_COUNTS": True,  # Show instances counts for each model
    # "APP_ICONS": {  # Set icons for applications(lowercase), including 3rd party apps, {'application_name': 'material_icon_name', ...}
    #     "sites": "send",
    # },
    # "MODEL_ICONS": {  # Set icons for models(lowercase), including 3rd party models, {'model_name': 'material_icon_name', ...}
    #     "site": "contact_mail",
    # },
}


ROOT_URLCONF = "web_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "web_project.wsgi.application"


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = ((os.path.join(BASE_DIR, "static")),)


MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "userapp.User"


LOGIN_REDIRECT_URL = reverse_lazy("core:home")
LOGOUT_REDIRECT_URL = reverse_lazy("core:home")
