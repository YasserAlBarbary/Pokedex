from third_party_api.poke_api import get_pokemon_thirdparty


def card_creator(pokemon_name):
    response = get_pokemon_thirdparty(pokemon_name)
    if response.status_code == 200:

        pokemonCard = {}

        pokemonCard['name'] = pokemon_name
        pokemonCard['habitat'] = response.json()['habitat']['name']
        print(response.json()['is_legendary'])
        pokemonCard['is_legendary'] = True if response.json()['is_legendary']==True else False

        for desc in response.json()['flavor_text_entries']:
            if desc['language']['name'] == 'en':
                pokemonCard['description'] = desc['flavor_text']
                break
        return pokemonCard
    elif response.status_code == 404:
        return {'Not Found.'}
    else:
        return {'An error has occurred.'}