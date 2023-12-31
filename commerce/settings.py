"""
Django settings for commerce project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import sys , os
from pathlib import Path 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-t7r@hsb^%7p!oa*nvu7%2y#t)rrtlbo*gwv^=28cvzc3yw+gyk"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['https://c0f9-39-62-25-239.ngrok-free.app', '*']


# Application definition

INSTALLED_APPS = [ 
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    "storeCommerce.apps.StorecommerceConfig",
    "Authentication.apps.AuthenticationConfig", 
    'storeCommerce.templatetags',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "commerce.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ['storeCommerce/templates','Authentication/templates'],
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

WSGI_APPLICATION = "commerce.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = False



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/



STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'statics')
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')





EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your email' # 'PinStore_Project.demo.django.login@gmail.com' 
EMAIL_HOST_PASSWORD = 'your email password'

NG = ""
LOCAL_HOST_STRIPE_Auth = 'http://localhost:8000/Auth'
LOCAL_HOST_STRIPE_Store = 'http://localhost:8000/store'
LOCAL_HOST_STRIPE_NG = NG + '/Auth/logIn'



# ------------------ Stripe integration -------------------
STRIPE_PUBLIC_KEY = "pk_test_******QDUzRcdw0ai84xqLsFylb0EVMCnP4Qv9y3NeW219gwQifI696lrqejOacOFEVO5bbIa3Zxd9bi5k7ON0sc200KlqO6***"
STRIPE_SECRET_KEY = "sk_test_******QDUzRcdw0aicbwC0jW25KusolDM0SPjbQxAau6bNtF097hPBYrS296qBWJMG8TqQbNCivSB21jUx3vClUjd00bAoD7***"
STRIPE_WEBHOOK_SECRET = "whsec_******fc793dd97e959535078ee4924688e48ba300703d002cef4346b27e1***"


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
