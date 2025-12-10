#Mohammedi Nour El Houda, BMC, 10/12/2025
#Ramdane Sarah
#Mokeddem Rachida
#Bouzara Aya
#Abidallah Aya Fatima Zohra

import pandas as pad

# Données : Séquences ADN, Longueur, Pourcentage de GC
data = {
     "Séquence":["ATGCGTACGTA", "GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA", "ATGAAAGGCTT", "CGTACGTAGC", "TTAACCGGAT"],
     "Longueur":[12, 12, 12, 10, 11, 10, 10],
     "Pourcentage GC":[50, 66.67, 58.33, 40, 45.45, 60, 50]
}

# Création d'un DataFrame (tableau pandas)
df = pad.DataFrame(data)
print("****** Creation et affichage ******")

#1) Affichage de tableau 
print("Tableau des séquences ADN :")
print(df)

#Opération sur les tableaux
print("****** Opération ******")

#2) Sélectionner la colonne "Longueur"
Longueur = df["Longueur"]
print(Longueurs)