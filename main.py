import requests

URL = "https://api.pokemonbattle.me/v2"
HEADER = {'Content-Type':'application/json', 
          'Trainer_token':'3b2b4167251b69c47cc335d2f5c90fb6'}
BODY = {
    "name": "generate",
    "photo": "generate"
}

response = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=BODY)
print(response.text)
ID = response.json()['id']

BODY = {
    "pokemon_id": ID,
    "name": "pikachu",
    "photo": "https://dolnikov.ru/pokemons/albums/010.png"
}
response = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=BODY)
print(response.text)


BODY = {
    "pokemon_id": ID
}
response = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=BODY)
print(response.text)