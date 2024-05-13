# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# packages
import random

print("Hello World")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# creation dictionnaire
mon_identite = {
    "nom": "Thomas",
    "age": 20,
    "ville": "Paris"
}
# affichage valeur d'une clé
print(mon_identite["age"])

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# boucle
list = [1,5,3] 
for n in list :
    print(n)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# fonction somme 
def addition(a, b, c):
    somme = a + b + c
    return somme

nombre1 = int(input("Entrez le premier chiffre entier : "))
nombre2 = int(input("Entrez le deuxième chiffre entier : "))
nombre3 = int(input("Entrez le troisième chiffre entier : "))

resultat = addition(nombre1, nombre2, nombre3)
print("Le résultat est :", resultat)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# utilisation module random - fonction randint
def random_sum(maximum) :
    nb1 = random.randint(0,maximum)
    nb2 = random.randint(0,maximum)
    somme = nb1+nb2
    return somme

resultat = random_sum(100)
print(resultat)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# utilisation module random - fonction choice  
def somme(liste):
    nb1 = random.choice(liste)
    print(nb1)
    nb2 = random.choice(liste)
    print(nb2)
    somme = nb1 + nb2
    return somme

list = [5, 10, 15, 20, 25, 30]
print(somme(list))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def aleatoire(bool, list=[], min=0, max=10) :
    if bool == True :
        return random.randint(min,max)
    else :
        return random.choice(list) 
        
print(aleatoire(False, list = [9,0,20,8,7,22,100,199992])) 
print(aleatoire(True, min=999, max=1000)) 
