from flask import Flask
import requests

app = Flask(__name__)
@app.route("/bonjour/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/aurevoir/")
def goodbye_world():
    return "Goodbye, World!"

@app.route("/pokemon/<name>")
def pokemon(name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_name = pokemon_data['name']
        pokemon_id = pokemon_data['id']
        return f"Name: {pokemon_name}, ID: {pokemon_id}"
    else:
        return "Pokemon not found!"
    
@app.route("/stw/<id>")
def starwars(id) :
    response2 = requests.get(f"https://swapi.dev/api/people/{id}")
    if response2.status_code == 200:
        stw_data = response2.json()
        stw_name = stw_data['name']
        stw_mass = stw_data['mass']
        return f"Name: {stw_name}, Mass: {stw_mass}"
    elif response2.status_code == 404:
        return "Character not found!"
 
app.run()