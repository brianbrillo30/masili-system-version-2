
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ci!=nl9#v4x=ve#$($=!h=bd9t)kl&*1_e)v)^_ln3d2g#pqqj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.ResidentManagement',
    'apps.UserPortal',
    'apps.Login',
    'apps.ClearanceManagement',
    'apps.IndigencyManagement',
    'apps.BusinessPermit',
    'apps.BuildingPermit',
    'apps.Dashboard',
    'apps.AdminProfile',
    'apps.ResidencyCertificate',
    'apps.AnnouncementManagement',
    'apps.ReportManagement',
    'crispy_forms',
    'crispy_bootstrap5',
    'django.contrib.humanize',
    'apps.RegisterOfficial',
    'apps.OfficialList',
    'apps.LoggedReports',
    'apps.RequestLogs',
    'captcha',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR) + '/templates/',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.UserPortal.context_processors.add_variable_to_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'
HASHIDS_SALT= 'some_random_string'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_masili',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost'
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
  
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL ='/media/'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'barangaymasili@gmail.com'
EMAIL_HOST_PASSWORD = 'mqlxjdpsgmirlnxz'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"


RECAPTCHA_PUBLIC_KEY = '6LfiGGAiAAAAAFqonG2L6LFsSHDhpOv6eLQBX72F'
RECAPTCHA_PRIVATE_KEY = '6LfiGGAiAAAAAJKvjrrYVe4ioa0oXIcLQ5L-KeAx'
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']


from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

