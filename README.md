# Auto-Rest-Models
Provides automatic REST API for models in Django project

# Requirements
- Python 3.8.2
- Django 3.0.8
- djangorestframework 3.11.0
- django-filter 2.3.0

# Installation
- Clone this repository:

```
cd
git clone https://github.com/ErnestIpekchyan/auto-rest-models.git
```

- Install `auto_rest_models` to your application:

```
pip install ~/auto-rest-models/dist/auto_rest_models-0.0.1-py3-none-any.whl
```

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

# Usage

- URL to get a list of objects (`GET` request):

```
/<app_name>/<model_name>
```

- URL to create an object (`POST` request):

```
/<app_name>/<model_name>
```

- URL to get the object (`GET` request):

```
/<app_name>/<model_name>/<pk>
```

- URL to update the object (`PUT` request):

```
/<app_name>/<model_name>/<pk>
```

- URL to delete the object (`DELETE` request):

```
/<app_name>/<model_name>/<pk>
```

- Filter objects with:

```
/<app_name>/<model_name>?field1=val1&field2=val2
```

- Sort objects with:

```
/<app_name>/<model_name>?ordering=field1 (sort in ascending order)
/<app_name>/<model_name>?ordering=-field1 (sort in descending order)
/<app_name>/<model_name>?ordering=field1,field2 (sort by multiple fields)
```

- Paginate objects with:

```
/<app_name>/<model_name>?limit=2
```

# Testing

- Copy the `~/auto-rest-models/tests/` app directory to the root of your application

- Add `tests` to INSTALLED_APPS in settings.py:

```
INSTALLED_APPS = [
    # other apps
    'tests',
]
```

- Install `pytest-django`:

```
pip install pytest-django
```

- Open `~/auto-rest-models/tests/pytest.ini` file and change `DJANGO_SETTINGS_MODULE` with:

```
DJANGO_SETTINGS_MODULE = <your_project_name>.settings
```

- Run tests with the following command:

```
pytest -s tests/
```