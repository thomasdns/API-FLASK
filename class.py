class Voiture:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y

    def avancer(self, distance):
        self.position_y += distance

    def reculer(self, distance):
        self.position_y -= distance

    def tourner_gauche(self,distance):
        self.position_x -= distance

    def tourner_droite(self,distance):
        self.position_x += distance

    def afficher_position(self):
        print("Position actuelle de la voiture : ({}, {})".format(self.position_x, self.position_y))

# Création d'une voiture à la position initiale (0, 0)
ma_voiture = Voiture(0, 0)

# Exécution du trajet
actions = ['avancer', 'tourner_droite', 'reculer', 'tourner_gauche']

for action in actions:
    if action == 'avancer':
        distance = int(input("Entrez la distance à avancer : "))
        ma_voiture.avancer(distance)
    elif action == 'reculer':
        distance = int(input("Entrez la distance à reculer : "))
        ma_voiture.reculer(distance)
    elif action == 'tourner_gauche':
        distance = int(input("Entrez la distance à tourner a gauche : "))
        ma_voiture.tourner_gauche(distance)
    elif action == 'tourner_droite':
        distance = int(input("Entrez la distance à tourner à droite : "))
        ma_voiture.tourner_droite(distance)
    ma_voiture.afficher_position()
