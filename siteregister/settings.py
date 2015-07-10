"""
Django settings for siteregister project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm7w!-%f9a!^)1m-l=4_o@kwwol(@mzh3+o)lwc90+0!21=y*+x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'loginsys',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'siteregister.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR+"/templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'siteregister.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    ('static', '/home/michail/djangoenv/bin/siteregister/static'),
)
TEMPLATE_DIRS = (
    '/home/michail/djangoenv/bin/siteregister/templates',
    '/home/michail/djangoenv/bin/siteregister/loginsys/templates'
)

AUTHENTICATION_BACKENDS = (
	'social.backends.facebook.FacebookAppOAuth2',
	'social.backends.facebook.FacebookOAuth2',
	'social.backends.twitter.TwitterOAuth',
	'social.backends.vk.VKOAuth2',
	'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_TWITTER_KEY = 'TnbGnRWlQRqlXu4X4k528sKUJ'
SOCIAL_AUTH_TWITTER_SECRET = 'JQmbvRZlIFqkwLV7Amu5QsC9dH4SpDXFKWlJw7Ba5S6LCp7fLQ'

SOCIAL_AUTH_FACEBOOK_KEY = '856540591091892'
SOCIAL_AUTH_FACEBOOK_SECRET = 'e1064b15767024836f1136520637e790'

SOCIAL_AUTH_VK_OAUTH2_KEY = '4990446'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'JBnmcPlaJEMoIESmJu75'