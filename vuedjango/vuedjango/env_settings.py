import os
from django.core.exceptions import ImproperlyConfigured


def get_env_value(env_variable):
    try:
        return os.environ[env_variable]
    except KeyError:
        error_msg = f'Set the {env_variable} environment variable'
        raise ImproperlyConfigured(error_msg)


ALLOWED_HOSTS = []
SECRET_KEY = get_env_value('VUEDJANGO_SECRET_KEY')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_value('VUEDJANGO_DATABASE_NAME'),
        'USER': get_env_value('VUEDJANGO_DATABASE_USER'),
        'PASSWORD': get_env_value('VUEDJANGO_DATABASE_PASSWORD'),
        'HOST': get_env_value('VUEDJANGO_DATABASE_HOST'),
        'PORT': get_env_value('VUEDJANGO_DATABASE_PORT'),
    }
}

if get_env_value('VUEDJANGO_PRODUCTION') == 'FALSE':
    DEBUG = True
elif get_env_value('VUEDJANGO_PRODUCTION') == 'TRUE':
    ALLOWED_HOSTS = ['*']
    DEBUG = False
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
