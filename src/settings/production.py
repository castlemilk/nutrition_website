

# using webfaction

#username: castlemilk
#password: ********
#application: nutrition_page
#database:
#name : nutrition_page
#postgressql
#username: castlemilk
#password: ********

#static is @ n_static


"""
Django settings for src project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.conf import settings

if not settings.DEBUG:
    print "using production settings"
    import os

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'kf9p%-omfn^ng_^)f3#d_%4@@i6tdi!a#fdop5=0gly@bq10jk'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False

    ALLOWED_HOSTS = ['castlemilk.webfactional.com']


    # Application definition

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'registration',
        'crispy_forms',
        'newsletter',

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

    ROOT_URLCONF = 'src.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                        os.path.join(BASE_DIR, 'templates'),
                    ],
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

    WSGI_APPLICATION = 'src.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/1.8/ref/settings/#databases
    from .db_password import DBPASS
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': "nutrition_page",
            'USER': "castlemilk",
            'PASSWORD': DBPASS,
        }
    }


    # Internationalization
    # https://docs.djangoproject.com/en/1.8/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'Australia/Melbourne'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.8/howto/static-files/

    STATIC_URL = '/static/'
    #STATIC_ROOT = '/var/www/example.com/static/'
    # STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),'static_in_env', 'static_root')
    STATIC_ROOT = '/home/castlemilk/webapps/n_static/'
    STATICFILES_DIRS = (
                        os.path.join(BASE_DIR,'static_in_pro', 'our_static'),
                      )

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),'static_in_env', 'media_root')
    MEDIA_ROOT = '/home/castlemilk/webapps/n_static/'


    #email config
    from .email_settings import EMAIL_ADDRESS, EMAIL_PASSWORD
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = EMAIL_ADDRESS
    EMAIL_HOST_PASSWORD = EMAIL_PASSWORD
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True

    '''
    To get this working with Gmail accounts the capture system needs to be modified
    In order to do thi follow the link:
        https://accounts.google.com/displayunlockcaptcha
    '''


    # django registration redux settings:
    ACCOUNT_ACTIVATION_DAYS = 7
    REGISTRATION_AUTO_LOGIN = True
    SITE_ID=1
    LOGIN_REDIRECT_URL = '/'
    # crispy forms settings:
    CRISPY_TEMPLATE_PACK = 'bootstrap3'