"""
Django settings for HIA_Project project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
# from django.utils.translation import gettext as _
from pathlib import Path
import os
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR_CUSTOM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
git_helpdesk_path = os.path.join(BASE_DIR_CUSTOM, 'django-helpdesk')
git_blog_path = os.path.join(BASE_DIR_CUSTOM, 'djangocms-blog')
sys.path.insert(0, git_helpdesk_path)
sys.path.insert(0, git_blog_path)
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-27aad8z4v2ojvabbl0!oasdd+#f)s4el2_t20^*c#giq)_%38)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1
# Application definition

INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'cms',
    'menus',
    'treebeard',
    'sekizai',
    'mptt',
    'djangocms_text_ckeditor',
    'djangocms_link',
    'djangocms_file',
    'djangocms_picture',
    'djangocms_video',
    'djangocms_googlemap',
    'djangocms_snippet',
    'djangocms_style',
    'django.contrib.humanize',  # Required for elapsed time formatting
    'bootstrap4form', # Required for nicer formatting of forms with the default templates
    'account',  # Required by pinax-teams
    'pinax.invitations',  # Required by pinax-teams
    'pinax.teams',  # Team support
    'reversion',  # Required by pinax-teams
    'rest_framework',  # required for the API
    'helpdesk',  # This is us!
    'aldryn_forms',
    'aldryn_forms.contrib.email_notifications',
    'emailit',
    'filer',
    'easy_thumbnails',
    'aldryn_apphooks_config',
    'parler',
    'taggit',
    'taggit_autosuggest',
    'meta',
    'sortedm2m',
    'djangocms_blog',
    'aldryn_search'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
]

X_FRAME_OPTIONS = 'SAMEORIGIN'

THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

META_SITE_PROTOCOL = 'http'  # set 'http' for non ssl enabled websites
META_USE_SITES = True

META_USE_OG_PROPERTIES=True
META_USE_TWITTER_PROPERTIES=True
META_USE_GOOGLEPLUS_PROPERTIES=True # django-meta 1.x+
META_USE_SCHEMAORG_PROPERTIES=True  # django-meta 2.x+

ROOT_URLCONF = 'HIA_Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
                'django.template.context_processors.i18n'
            ],
        },
    },
]

CMS_TEMPLATES = [
    ('index.html', 'Home Page'),
]

WSGI_APPLICATION = 'HIA_Project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGES = [
    ('en', 'English'),
]

LANGUAGE_CODE = 'en'

PARLER_LANGUAGES = {
    1: (
        {'code': 'en',},
        # {'code': 'it',},
        # {'code': 'fr',},
    ),
    'default': {
        'fallbacks': ['en'],
    }
}

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# Your project will probably also have static assets that aren’t tied to a particular app. 
# In addition to using a static/ directory inside your apps, you can define a list of directories

# STATICFILES_DIRS = [
#     BASE_DIR / "static",
#     '/var/www/static/',
# ]

# STATIC_ROOT = "/var/www/example.com/static/" for production
# python manage.py collectstatic

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/helpdesk/login/'

BLOG_AVAILABLE_PERMALINK_STYLES = (
    ('full_date', ('Full date')),
    ('short_date', ('Year /  Month')),
    ('category', ('Category')),
)

BLOG_PERMALINK_URLS = {
    "full_date": "<int:year>/<int:month>/<int:day>/<str:slug>/",
    "short_date": "<int:year>/<int:month>/<str:slug>/",
    "category": "<str:category>/<str:slug>/",
}

# CKEDITOR_ALLOW_NONIMAGE_FILES = False

CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'toolbar_CMS': [
        ['Undo', 'Redo'],
        ['cmsplugins', '-', 'ShowBlocks'],
        ['Format', 'Styles'],
    ],
    'skin': 'moono-lisa',
    'toolbar': 'Full',
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
# EMAIL_HOST_USER ='lomaz.9999@gmail.com'
# EMAIL_HOST_PASSWORD = '***'

# DEFAULT_FROM_EMAIL = 'testmail@gmail.com'

# HAYSTACK_ROUTERS = ['aldryn_search.router.LanguageRouter',]
