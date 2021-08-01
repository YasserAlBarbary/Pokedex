import requests

def get_pokemon_thirdparty(pokemon_name):
    return requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{pokemon_name}/')
