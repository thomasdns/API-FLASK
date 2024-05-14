import requests
pikachu_data = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
pikachu_json = pikachu_data.json()
# print(pikachu_json["name"])


def combat(name1,name2) :
    pokemon1_data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name1}").json()
    pokemon2_data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name2}").json()
    order1 = pokemon1_data["order"]
    order2 = pokemon2_data["order"]

    if order1 > order2 :
        print(f"{name1.capitalize()} is better than {name2}.")
    elif order1 < order2 :
        print(f"{name2.capitalize()} is better than {name1}.")
    else :
        print(f"{name1.capitalize()} and {name2.capitalize()} have the same order.")

print(combat("pidgeot", "pikachu"))

# f permet de formater pour mettre une variable
# la méthode capitalize permet d'avoir la première lettre en majuscule et les autres en minuscule