#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python 3.7
import os
from glob import iglob
def renomme(repertoire, motifs=['*.ini'], entete="en-GB.", affiche=False):
    """Trouve tous les fichiers du répertoire et de ses sous-répertoires
       satisfaisant aux motifs wildcard, et les renomme en leur retirant
       l'en-tête de leur nom 
    """
    # normalise le chemin
    repertoire = os.path.abspath(os.path.expanduser(repertoire))
    # renomme les fichiers
    nbfichiers = 0
    for motif in motifs:
        for fichier in iglob(os.path.join(repertoire, "**", motif), recursive=True):
            if os.path.isfile(fichier): # on ne s'intéresse qu'aux fichiers
                # sépare le chemin et le nom de fichier
                chemin, nom = os.path.split(fichier)
                # calcule le nouveau nom
                if nom.startswith(entete):
                    # ici, il faut renommer!
                    nom = nom[len(entete):] # supprime l'en-tête
                    # recalcule le nouveau nom du fichier avec son chemin    
                    fichier2 = os.path.join(chemin, nom)
                    # renomme
                    try:
                        os.rename(fichier, fichier2) 
                        nbfichiers += 1
                    except WindowsError:
                        os.remove(fichier)
                        os.rename(fichier, fichier2) 
                    if affiche: print("Fichier renommé:", fichier, "===>", fichier2)  
 
    return nbfichiers # nombre de fichiers renommés
	
repertoire = r"C:\Users\yannick\Documents\GitHub\flexicontent-translations"
nbfichiers = renomme(repertoire, motifs=['*.ini'], entete="en-GB.", affiche=True)
Print("Nombre de fichiers renommés:", nbfichiers)
