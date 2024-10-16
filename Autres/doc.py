import json

# Menu d'options
maListe = [
    "1: Ajouter un élément à la liste",
    "2: Retirer un élément de la liste",
    "3: Afficher la liste",
    "4: Vider la liste",
    "5: Quitter"
]

# Liste de courses vide au départ
listEmpty = []

# Affichage initial de la liste vide et du menu
print("Liste actuelle:", listEmpty)
for option in maListe:
    print(option)

while True:
    try:
        choix = int(input('Votre choix est (1-5): '))
        
        if choix < 1 or choix > 5:
            print('Veuillez entrer un numéro valide (1-5).')
            continue

        if choix == 1:  # Ajouter un élément à la liste
            data = input("Indique l'élément à ajouter: ")
            listEmpty.append(data)
            print("Élément ajouté:", listEmpty)

        elif choix == 2:  # Retirer un élément de la liste
            if listEmpty:
                listEmpty.pop()
                print("Un élément a été retiré:", listEmpty)
            else:
                print("La liste est déjà vide, impossible de retirer.")

        elif choix == 3:  # Afficher la liste
            if not listEmpty:
                print("La liste est vide.")
            else:
                print("Liste actuelle:", listEmpty)

        elif choix == 4:  # Vider la liste
            listEmpty.clear()
            print("La liste a été vidée.")

        elif choix == 5:  # Quitter
            print("Sortie du programme.")
            break

    except ValueError:
        print("Veuillez entrer un nombre valide.")

# Sauvegarde de la liste dans un fichier JSON
with open('data.json', "w") as f:
    json.dump(listEmpty, f, indent=4)
    print("La liste a été sauvegardée dans 'data.json'.")
