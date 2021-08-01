from third_party_api.shakespear_translator import translate_to_shakespear
from third_party_api.yoda_translator import translate_to_yoda


def translate_description(pokemon_card):
    if pokemon_card['habitat'] =='cave' or pokemon_card['is_legendary']:
        response = translate_to_yoda(pokemon_card['description'])
    else:
        response = translate_to_shakespear(pokemon_card['description'])
    if response.status_code == 200:
        pokemon_card['description'] = response.json()['contents']['translated']
    return pokemon_card