import requests

def translate_to_yoda(description):
    url = f"https://api.funtranslations.com/translate/yoda.json?text={description!r}"
    response = requests.request("GET", url)

    return response