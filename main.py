def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom


def demander_age():
    age_int = 0
    while age_int == 0:
        age_str = input("Quel est votre âge ? ")
        try:
            age_int = int(age_str) # Convertir la chaîne de caractères en entier, j'ai fait comme ça mais c'est juste pour la concaténation avec + 
        except:
            print("ERREUR: Vous devez rentrer un nombre pour l'âge.")
    return age_int

nom = demander_nom()
age = demander_age()



print(f"Vous vous appelez {nom}. Vous avez {age} ans.")
print(f"L'année prochaine vous aurez {age + 1} ans.")


