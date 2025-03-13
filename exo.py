import random

nb = random.randint(0, 10)  # Génère un nombre aléatoire
nbuser = int(input("Entrez un chiffre entre 0 et 10 : "))

for i in range(10):
    if nb == nbuser:
        print("Bien joué !")
        break  # Sort de la boucle si la réponse est correcte
    else:
        nbuser = int(input("Mauvais choix, essaye encore : "))

if nb != nbuser:
    print(f"Dommage, le nombre était {nb}.")
