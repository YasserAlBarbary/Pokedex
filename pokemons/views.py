from rest_framework import generics

from services.pokemon_card_creator import card_creator
from .models import Pokemon
from .serializers import PokemonSerializer

from rest_framework import views
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PokemonCardView(views.APIView):
    # queryset = Pokemon.objects.all()
    # lookup_field = 'name'
    # serializer_class = PokemonSerializer
    def get(self, request, name):

        pokemon_card = card_creator(name)
        results = PokemonSerializer(pokemon_card).data
        return Response(results)

class PokemonCardTranslatedView(generics.RetrieveAPIView):
    queryset = Pokemon.objects.all()
    lookup_field = 'name'
    serializer_class = PokemonSerializer
