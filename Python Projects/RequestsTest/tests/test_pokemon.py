import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '96649ad6aebe0cf1fb99282e5ca2ee73'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '33490'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200