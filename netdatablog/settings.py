"""
Django settings for netdatablog project.

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
SECRET_KEY = 'c40h^73to5*pb9#ba3#*@vuj+an0l!*@68=x%84byq=uho@zhz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
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

ROOT_URLCONF = 'netdatablog.urls'

WSGI_APPLICATION = 'netdatablog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
if 'SERVER_SOFTWARE' in os.environ:
    MYSQL_HOST = 'rdsrayzenzjnv7v.mysql.rds.aliyuncs.com'
    MYSQL_PORT = 3306
    MYSQL_USER = 'chongwug'
    MYSQL_PASS = 'weet6321'
    MYSQL_DB = 'chongwug'
else:
    # Make `python manage.py syncdb` works happy!
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PASS = 'root'
    MYSQL_DB = 'datablog'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': MYSQL_DB,
        'USER': MYSQL_USER,                      # Not used with sqlite3.
        'PASSWORD': MYSQL_PASS,                  # Not used with sqlite3.
        'HOST': MYSQL_HOST,                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': MYSQL_PORT,                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(os.path.split(os.path.dirname(__file__))[0], 'static/blog/tpl').replace('\\','/'),
)