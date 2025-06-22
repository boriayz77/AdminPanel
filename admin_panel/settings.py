
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

SECRET_KEY = '123'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'dashboard',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
]

ROOT_URLCONF = 'admin_panel.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'dashboard' / 'templates'],
    'APP_DIRS': True,
    'OPTIONS': {'context_processors': []},
}]

STATIC_URL = '/static/'
