import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1$(46qw^uc2q&c)gad(*4^y)a8g2^dbr$%)nlvyf3jygfbv70('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # - The Django admin system
    'django.contrib.admin',

    # - The authentication system
    'django.contrib.auth',

    # - Framework for content types
    'django.contrib.contenttypes',

    # - Session Framework
    'django.contrib.sessions',

    # - Message Framework
    'django.contrib.messages',

    # - Manages static files
    'django.contrib.staticfiles',

    'cars.apps.CarsConfig',
    'signup.apps.SignupConfig',
]

# 6 We can add data to the DB using the Python shell
# - python3 manage.py shell
# - Import Models : from cars.models import Question, Choice
# - Display Questions : Question.objects.all()
# - Create a Question
# - from django.utils import timezone
# - q = Question(question_text="What's New?", pub_date=timezone.now())
# - Save to the DB : q.save()
# - Get the questions id : q.id
# - Get the questions text : q.question_text
# - Get the pub date : q.pub_date
# - Change the question : q.question_text = "What's Up?"
# - Save the change : q.save()
# - Display Questions : Question.objects.all()

# 6 Change cars/models.py to provide more info on question and choice

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
              
]

ROOT_URLCONF = 'carprowler.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'carprowler.wsgi.application'

# 4 Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# 4 We'll use the default database of SQLite3
# - You can use other DBs, but must add USER, PASSWORD and HOST
# - django.db.backends.mysql
# - django.db.backends.postgresql
# - django.db.backends.oracle

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

# - Change the time zone to yours using
# - https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

# - Add a path for static files
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

