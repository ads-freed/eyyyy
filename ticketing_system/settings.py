import os
from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-production-secret-key')

# --------------------
# Production Settings
# --------------------
DEBUG = False

#ALLOWED_HOSTS = ['your_domain.com', 'www.your_domain.com', 'server_IP']
ALLOWED_HOSTS = ['server_IP']

# Application definition
INSTALLED_APPS = [
    # Default Django apps:
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party apps:
    'ckeditor',
    'crispy_forms',
    'widget_tweaks',
    'channels',
    # Local apps:
    'accounts',
    'tickets',
    'chat',
    'cms',
    'logs',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # For multilingual & RTL support
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ticketing_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Global templates directory if needed
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'ticketing_system.context_processors.theme',
            ],
        },
    },
]

WSGI_APPLICATION = 'ticketing_system.wsgi.application'
ASGI_APPLICATION = 'ticketing_system.asgi.application'

# ----------------
# Database Setup
# ----------------
# For production, using PostgreSQL is recommended. Environment variables can be set for security.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Change to 'django.db.backends.mysql' for MySQL
        'NAME': os.environ.get('DJANGO_DB_NAME', 'eyyyydb'),
        'USER': os.environ.get('DJANGO_DB_USER', 'eyyyy'),
        'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD', 'eyyyy'),
        'HOST': os.environ.get('DJANGO_DB_HOST', 'localhost'),
        'PORT': os.environ.get('DJANGO_DB_PORT', '5432'),
    }
}

# -----------------------
# Internationalization
# -----------------------
LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', 'English'),
    ('ar', 'Arabic'),
    ('ja', 'Japanese'),
]
LOCALE_PATHS = [BASE_DIR / 'locale']

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# -------------------------------
# Static & Media Files Settings
# -------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# -------------------
# Third-Party Configs
# -------------------
# CKEditor configuration
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
    },
}

# Crispy Forms configuration
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Channels configuration for real-time features (using an in-memory layer for simple setups)
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}

# Email settings for notifications (update with your credentials)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.yourserver.com')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 587)
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'your_email@yourserver.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'your_email_password')
EMAIL_USE_TLS = True

# -------------------
# Custom Context Processors
# -------------------
# The 'ticketing_system.context_processors.theme' context processor passes theme settings (light/dark mode) to templates.
