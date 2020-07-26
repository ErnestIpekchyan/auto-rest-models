# Auto-Rest-Models
Provides automatic REST API for models in Django project

# Requirements
- Python 3.8.2
- Django 3.0.8
- djangorestframework 3.11.0

# Installation
- Clone this repository

```https://github.com/ErnestIpekchyan/auto-rest-models.git```

- Install `auto_rest_models` to your application

```pip install ~/auto_rest_models/dist/auto_rest_models-0.0.1-py3-none-any.whl```

- Add `auto_rest_models` to INSTALLED_APPS in settings.py:

```
INSTALLED_APPS = [
    # other apps
    'auto_rest_models',
]
```

- Include `auto_rest_models.urls` in your urls.py:

```
urlpatterns += [
    path('', include('auto_rest_models.urls'))
]
```