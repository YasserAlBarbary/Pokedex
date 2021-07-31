from rest_framework import generics
from .models import Pokemon
from .serializers import PokemonSerializer


class DetailPokemon(generics.RetrieveAPIView):
    queryset = Pokemon.objects.all()
    lookup_field = 'name'
    serializer_class = PokemonSerializer