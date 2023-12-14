# settings_ci.py

from .settings import *

# Configuration de la base de données pour les tests CI
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
