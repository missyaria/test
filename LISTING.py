import os
path = os.getcwd()
print(f"Vous vous trouvez actuellement dans le répertoire suivant : {os.getcwd()}")
print(f"Ce répertoire contient les fichiers suivants : {os.listdir(path)}")
close=input("Appuyez sur entrée pour quitter")
