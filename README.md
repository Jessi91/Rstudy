### RStudy   

[![Django CI](https://github.com/Jessi91/Rstudy/actions/workflows/django.yml/badge.svg)](https://github.com/Jessi91/Rstudy/actions/workflows/django.yml)
<!-- [![Build Status](https://app.travis-ci.com/Jessi91/Rstudy.svg?token=L98WEBS8FGkweyEqUq6x&branch=main)](https://app.travis-ci.com/Jessi91/Rstudy) -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/Jessi91/Rstudy/edit/main/LICENSE)


[![Latest Release](https://shields.io/github/release/Jessi91/Rstudy.svg)](https://github.com/Jessi91/Rstudy/releases/)




[![GitHub tag (with filter)](https://shields.io./github/v/tag/Jessi91/Rstudy)](https://github.com/Jessi91/Rstudy/tag/)


![GitHub contributors](https://shields.io./github/contributors/Jessi91/Rstudy)


![GitHub Release Date - Published_At](https://shields.io./github/release-date/Jessi91/Rstudy)


![PyPI - Python Version](https://shields.io./pypi/pyversions/Django)




<!-- ### RStudy    [![Build Status](https://https://img.shields.io/travis/com/Jessi91/Rstudy.svg?token=L98WEBS8FGkweyEqUq6x&branch=main)](https://travis-ci.com/github/Jessi91/Rstudy) -->

## Configuration environnement
- Activer Mysql
- Copier le fichier `RStudy/RStudy/settings_default.py` and rename `RStudy/RStudy/settings.py`
- Set the settings file for your DB :
```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # DataBase Name
        'NAME': 'rstudy',

        'USER': 'root',
        'HOST' : 'localhost',
        'PORT' : '3306',
        
        # Your password
        'PASSWORD' : '',
    }
}
```
> Nous recommandons l'utilisation d'un environement virtuel (venv) pour palier à tous problèmes de versionages, la procédure est simple : 
```
python -m venv venv
```
- Activons le venv :
- Pour installer les librairies ayant les versions nécessaires (Elles sont inscrites dans), vous avez seulement à tapper la commande ci-dessous :  
```
make install
```

## Migrer les données 

1. Se mettre dans le path du repo 
2. Se mettre dans le path du l'app RStudy avec la commande => ```cd RStudy```

3. Pour réaliser des migrations des données soit, transformer le code python de 'models.py' en du code sql
```
python manage.py makemigrations
```
4. Pour transfer à la base de données :
```
python manage.py migrate
```

## Pour démmarer le server
1. Se mettre dans le path du repo 
2. Se mettre dans le path du l'app RStudy avec la commande => ```cd RStudy```
3. Run le server avec la commande ```py manage.py runserver```

**creer un admin**
```py manage.py createsuperuser```
