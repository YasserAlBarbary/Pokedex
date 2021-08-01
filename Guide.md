# Pokedex API [Django Draft]

## What needs to be installed 
* Python3 
* pipenv
## Testing with custom Data First
### Installing Django and prepare your env
``` Bash
mkdir Pokedex && cd Pokedex
pipenv install django~=3.1.0
pipenv shell
```
### Create Django project
```bash
django-admin startproject config .
```
### Create Pokemons App in your Django Pokedex project
```bash
python manage.py startapp pokemons
python manage.py migrate
```
### Add Pokemons App to your Django Project
```Python
# config/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local
    'pokemons', # new
]
```
**Check That your project runs with **

​	```$ python manage.py runserver```

**Exit with** `ctrl + c` 

### Add a Model for Pokemons
```python
# pokemons/models.py
from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    habitat = models.CharField(max_length=100)
    is_legendary = models.CharField(max_length=13)
    
    def __str__(self):
    	return self.name
```
### Migrate the new model
```bash
$ python manage.py makemigrations pokemons
$ python manage.py migrate
```
### Create an admin user
```Bash
$ python manage.py createsuperuser
```

### Register the Admin to pokemons App
```Python 
# pokemons/admin.py
from django.contrib import admin
from .models import Pokemon

admin.site.register(Pokemon)
```

### Add DRF - Django REST Framework
```bash
pipenv install djangorestframework~=3.11.0
```
### Add rest_framework to the INSTALLED_APPS config 
```Python
# config/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party
    'rest_framework', # new

    # Local
    'pokemons',
]

# new
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
    	'rest_framework.permissions.AllowAny',
    ]
}
```
### Add URL file for routing 
```python
# config/urls.py
from django.contrib import admin
from django.urls import include, path # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pokemon/', include('pokemons.urls')), # new
]
```
### create our app-level pokemons/urls.py file
```Bash
$ touch pokemons/urls.py
```
```python
# todos/urls.py
from django.urls import path
from .views import DetailPokemon
    urlpatterns = [
    path('<str:name>/', DetailPokemon.as_view()),
]
```
### Add a serializer for the pokemons endpoints
```Bash
$ touch todos/serializers.py
```
```python
# todos/serializers.py
from rest_framework import serializers
from .models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('id', 'name', 'description', 'habitat', 'is_legendary')
```
### Add view to your Pokemon App
```Python
# pokemons/views.py
from rest_framework import generics
from .models import Pokemon
from .serializers import PokemonSerializer


class DetailPokemon(generics.RetrieveAPIView):
    queryset = Pokemon.objects.all()
    lookup_field = 'name'
    serializer_class = PokemonSerializer
```
### Test the API
* Go to the Admin portal on localhost/admin/
* Add a Couple of Pokemons
* use the API to call the pokemons 
	example: ```http://127.0.0.1:8000/pokemon/mewtwo/``` 
### Test it again with unit tests
```python 
# pokemons/tests.py
from django.test import TestCase
from .models import Pokemon


class PokemonModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Pokemon.objects.create(
            name="pikachu",
            description='''When several of these POKéMON gather, their electricity could build and cause lightning storms.''',
            habitat="forest",
            is_legendary=False,
        )

    def test_description_content(self):
        pokemon = Pokemon.objects.get(name="pikachu")
        expected_object_name = f'{pokemon.description}'
        self.assertEqual(expected_object_name, '''When several of these POKéMON gather, their electricity could build and cause lightning storms.''')

    def test_name_content(self):
        pokemon = Pokemon.objects.get(name="pikachu")
        expected_object_name = pokemon.name
        self.assertEqual(expected_object_name, "pikachu")

    def test_body_content(self):
        pokemon = Pokemon.objects.get(name="pikachu")
        expected_object_name = pokemon.habitat
        self.assertEqual(expected_object_name, "forest")

    def test_is_legendary_content(self):
        pokemon = Pokemon.objects.get(name="pikachu")
        expected_object_name = f'{pokemon.is_legendary}'
        print("legend?",expected_object_name)
        self.assertTrue(expected_object_name, False)


```
Run in bash
```bash
$ python manage.py test
```

# use APIView(call 3rd prty GET here) , Serlizers 

```python
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
```

### Create a new api app

```Bash
python manage.py startapp api
```
### Then add it to INSTALLED_APPS.
```Python
# config/settings.py
INSTALLED_APPS = [
    # Local
    'pokemons.apps.PokemonsConfig',
    'api.apps.ApiConfig', # new
    # 3rd party
    'rest_framework',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
### Add api route
```Python
# config/urls.py
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('pokemon/', include('api.urls')), # new
]
```
### Create a urls.py file within the api app
```Bash
touch api/urls.py
```



