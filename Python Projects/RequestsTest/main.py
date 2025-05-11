import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '96649ad6aebe0cf1fb99282e5ca2ee73'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_create = {
    "name": "generate",
    "photo_id": -1
}
body_full_upd = {
    "pokemon_id": "312737",
    "name": "New Name",
    "photo_id": 2
}
body_add_pokeball = {
    "pokemon_id": "312737"
}


response_create = requests.post(
        url = f'{URL}/pokemons',
        headers = HEADER,
        json = body_create
    )
print(response_create.text)


response_full_upd = requests.put(
        url = f'{URL}/pokemons',
        headers = HEADER,
        json = body_full_upd
    )
print(response_full_upd.text)


response_add_pokeball = requests.post(
        url = f'{URL}/trainers/add_pokeball',
        headers = HEADER,
        json = body_add_pokeball
    )
print(response_add_pokeball.text)
