from pathlib import Path
import shutil

# Chemin du répertoire source
p = Path("/Users/moussa/Desktop/py")

# Itérer sur les éléments dans le répertoire
for i in p.iterdir():
    if i.is_file():  # S'assurer que c'est un fichier, pas un répertoire
        # Construire les chemins de destination
        put_file_Videos = p / "Videos" / i.name
        put_file_Musique = p / "Musique" / i.name
        put_file_Images = p / "Images" / i.name
        put_file_Autres = p / "Autres" / i.name

        # Vérifier l'extension et déplacer le fichier dans le bon dossier
        # Vidéos
        if i.suffix in [".avi", ".mp4", ".gif"]:
            shutil.move(str(i), str(put_file_Videos))  # Utilise `i` comme source
        # Musique
        elif i.suffix in [".mp3", ".wav", ".flac"]:
            shutil.move(str(i), str(put_file_Musique))
        # Images
        elif i.suffix in [".bmp", ".png", ".jpg"]:
            shutil.move(str(i), str(put_file_Images))
        # Autres fichiers
        else:
            shutil.move(str(i), str(put_file_Autres))

print("Fichiers déplacés avec succès !")
