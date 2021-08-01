from rest_framework import generics

from services.pokemon_card_creator import card_creator
from services.pokemon_description_translator import translate_description
from .models import Pokemon
from .serializers import PokemonSerializer

from rest_framework import views
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PokemonCardView(views.APIView):

     def get(self, request, name):

        pokemon_card = card_creator(name)
        result = PokemonSerializer(pokemon_card).data
        return Response(result)


class PokemonCardTranslatedView(views.APIView):

    def get(self, request, name):
        pokemon_card = card_creator(name)
        pokemon_card = translate_description(pokemon_card)
        result = PokemonSerializer(pokemon_card).data
        return Response(result)
