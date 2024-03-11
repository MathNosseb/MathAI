import couleur
with open("C:\\Users\\MATHEO.BESSON\\Documents\\autre\\codage\\python\\ia\\data.txt", "r+", encoding='utf-8') as data:
    # Lecture du contenu du fichier
    ligne_count = 0
    print()
    print()
    print(couleur.colorise("g Bienvenue sur MathAI, le robot de Mathéo \n pour quitter et sauvegarder les majs, taper 'q'"))
    print()

    # Lire les lignes du fichier et les stocker dans une liste
    lignes = data.readlines()

    while True:
        # Demande de l'entrée utilisateur
        trust_line = []
        print()
        user_words = input("user input: ")
        print()
        reponse = user_words

        # Vérification pour quitter
        if user_words.lower() == 'q':
            print("Aurevoir sur mon ChatGPT")
            break

        # Réinitialiser le compteur de lignes pour chaque nouvelle recherche
        ligne_count = 0

        # Découpage de l'entrée utilisateur en mots
        user_words = user_words.replace('-', ' ').split()

        # Parcourir chaque mot de l'entrée utilisateur
        for mot in user_words:
            ligne_count = 0  # Réinitialiser le compteur de lignes pour chaque mot
            for ligne in lignes:
                ligne_count += 1
                if mot in ligne and not ligne.startswith("ChatGPT :"):
                    trust_line.append(ligne_count)

        # Compter les occurrences de chaque ligne
        occurrences = {x: trust_line.count(x) for x in set(trust_line)}

        # Trouver la ligne avec le plus grand nombre d'occurrences
        try:
            element_max_occurrences = max(occurrences, key=occurrences.get)
            #print("La ligne avec le plus d'occurrences est :", element_max_occurrences)
            print()
            print(lignes[element_max_occurrences].strip())
            print()
            print("Est-ce que cette réponse vous convient-elle?")
            print()
            choix = input("oui/non : ")
            print()
            if choix.lower() == "non":
                print()
                new_reponse = input("Réponse : ")
                print()
                lignes.append(reponse + "\n")
                lignes.append("ChatGPT :" + new_reponse + "\n")
                print()
                print("Merci de votre contribution !")
                print()
        except ValueError:
            print("Je ne sais pas quoi répondre")
            print("Voulez-vous donner la réponse pour améliorer l'IA ?")
            choix = input("oui/non : ")
            if choix.lower() == "oui":
                new_reponse = input("Réponse : ")
                lignes.append(reponse + "\n")
                lignes.append("ChatGPT :" + new_reponse + "\n")
                print("Merci de votre contribution !")

    # Réécrire toutes les lignes dans le fichier
    data.seek(0)
    data.writelines(lignes)
