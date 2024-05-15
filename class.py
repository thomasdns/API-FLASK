class Voiture:
    def __init__(self, marque, couleur, vitesse_max, quantite_essence):
        self.marque = marque
        self.couleur = couleur
        self.vitesse_max = vitesse_max
        self.quantite_essence = quantite_essence
        self.position = 0
        self.vitesse_actuelle = 0

    def avancer(self, distance):
        if self.vitesse_actuelle > 0:
            self.position += distance * self.vitesse_actuelle
            print(f"{self.marque} avance de {distance} unités. Nouvelle position : {self.position}")
        else:
            print("La voiture est à l'arrêt.")

    def reculer(self, distance):
        if self.vitesse_actuelle > 0:
            self.position -= distance * self.vitesse_actuelle
            print(f"{self.marque} recule de {distance} unités. Nouvelle position : {self.position}")
        else:
            print("La voiture est à l'arrêt.")

    def changer_vitesse(self, nouvelle_vitesse):
        if nouvelle_vitesse <= self.vitesse_max:
            self.vitesse_actuelle = nouvelle_vitesse
            print(f"{self.marque} roule maintenant à {self.vitesse_actuelle} km/h.")
        else:
            print("La vitesse demandée dépasse la vitesse maximale de la voiture.")

    def ajouter_essence(self, quantite):
        self.quantite_essence += quantite
        print(f"{quantite} litres d'essence ajoutés. Nouvelle quantité d'essence : {self.quantite_essence} litres.")

# Création d'une instance de la classe Voiture
ma_voiture = Voiture("Toyota", "Rouge", 200, 50)

# Changer la vitesse de la voiture
ma_voiture.changer_vitesse(100)

# Avancer la voiture
ma_voiture.avancer(10)

# Ajouter de l'essence à la voiture
ma_voiture.ajouter_essence(20)