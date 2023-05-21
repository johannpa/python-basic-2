nom = ""

while nom == "":
    nom = input("Quel est votre nom ? ")

age = 0

while age == 0:
    age_str = input("Quel est votre âge ? ")
    try:
        age = int(age_str) # Convertir la chaîne de caractères en entier, j'ai fait comme ça mais c'est juste pour la concaténation avec + 
    except:
        print("ERREUR: Vous devez rentrer un nombre pour l'âge.")

# print("Fin de la boucle")


print(f"Vous vous appelez {nom}. Vous avez {age} ans.")
print(f"L'année prochaine vous aurez {age + 1} ans.")


