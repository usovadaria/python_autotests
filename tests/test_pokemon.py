import requests
import pytest

URL = "https://api.pokemonbattle.me/v2"
HEADER = {'Content-Type':'application/json'}
TOKEN = {'3b2b4167251b69c47cc335d2f5c90fb6'}
TRAINER_ID = '2499'

def test_status_code():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id' : TRAINER_ID})
    assert response.status_code == 200, "Unexpected status code"

def test_get_trainer_by_id():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id' : TRAINER_ID})
    assert response.json()["data"][0]['trainer_name'] == 'Дарьяша', 'Ups, wrong name'