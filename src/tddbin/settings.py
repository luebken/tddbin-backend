"""
Django settings for tddbin project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7ee1f+x2ggnk8^ys2nzzvn*#k()c%xz=5&&o_l8n9#hdb4%0@#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tddbin.urls'

WSGI_APPLICATION = 'tddbin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tddbin-backend',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'





#
# tddbin specific stuff
#

ALLOWED_HOSTS = [
    'localhost:8080',
    'tddbin.com',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tddbin-backend',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
    }
}

INSTALLED_APPS += (
    'core',
    'django_extensions',
    'werkzeug',
    'rest_framework', # see http://www.django-rest-framework.org
    'rest_framework_swagger', # An API documentation generator for Django REST Framework version see https://github.com/marcgibbons/django-rest-swagger
    'rest_framework.authtoken', # so we can use token auth for the REST API see http://www.django-rest-framework.org/api-guide/authentication#tokenauthentication
    'corsheaders',
)

MIDDLEWARE_CLASSES += (
    # 'werkzeug.debug.DebuggedApplication',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
}

SWAGGER_SETTINGS = {
    'exclude_namespaces': [], # List URL namespaces to ignore
    'api_version': '0.1',  # Specify your API's version
    'api_path': '/',  # Specify the path to your API not a root level
    'enabled_methods': [  # Specify which methods to enable in Swagger UI
        'get',
        'post',
        'put',
        'patch',
        'delete'
    ],
    'api_key': '', # An API key
    'is_authenticated': False,  # Set to True to enforce user authentication,
    'is_superuser': False,  # Set to True to enforce admin only access
}

CORS_ORIGIN_WHITELIST = (
    'localhost:8080', # for local dev
    'tddbin.com'
)
