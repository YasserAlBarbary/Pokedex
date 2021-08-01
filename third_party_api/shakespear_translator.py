
import requests

def translate_to_shakespear(description):
    url = f"https://api.funtranslations.com/translate/shakespeare.json?text={description!r}"
    response = requests.request("GET", url)

    return response