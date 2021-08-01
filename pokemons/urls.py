
from django.urls import path, URLPattern, URLResolver
from .views import PokemonCardView, PokemonCardTranslatedView

urlpatterns = [
    #path('translated/<str:name>/', PokemonCardTranslatedView.as_view()),
    path('<str:name>/', PokemonCardView.as_view()),
    ]