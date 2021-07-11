"""
Script pour créer une arborescence web
"""

import os

print("Création d'une structure de dossier web")

dir = input("Entrer un dossier\n")


if not os.path.exists(dir):
    print("Le dossier n'existe pas\n")
else:
    print("Les dossiers et fichiers suivants vont être créées :")
    print("\n\nDossier : ", dir)
    print("   │")
    print("   ├─ css")
    print("   │  │")
    print("   │  └─ style.css")
    print("   │")
    print("   ├─ js")
    print("   │  │")
    print("   │  └─ script.js")
    print("   │")
    print("   └─ index.php")

    #rep = "N"
    rep = input("\n\nConfirmer la création des éléments [Y/N]\n")
    
    if (rep == "Y") or (rep == "y"):
        
        file = dir + '\css'
        if not os.path.exists(file):
            os.mkdir(file)
        
        file = dir + '\js'
        if not os.path.exists(file):
            os.mkdir(file)
    
        file = dir + '\index.php'
        f = open(file, "a")
        f.close()
    
        file = dir + '\css\style.css'
        f = open(file, "a")
        f.close()
        
        file = dir + '\js\script.js'
        f = open(file, "a")
        f.close()
        
        print("La structure a été créée\n\n")
        
        rep = input("Ouvrir le dossier dans VSCode ? [Y/N]\n")
        if (rep == "Y") or (rep == "y"):
            os.system('code -n ' + dir)
            
    else:
        print("Annulation ...\nLa structure n'a pas été créée\n")


input("Appuyer sur une touche pour quitter.")