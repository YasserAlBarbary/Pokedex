
from django.urls import path, URLPattern, URLResolver
from .views import DetailPokemon

urlpatterns = [
        path('<str:name>/', DetailPokemon.as_view()),
    ]