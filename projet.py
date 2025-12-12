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

#3) filtrer les séquences avec une Longueur superieur à 10
print("************fltrage avec Longueur >10*************")
filtered_df=df[df["Longueur"]>10]
print(filtered_df)

#4) la moyenne de pourcentage GC
print("**************moyenne de Pourcentage GC%**************")
average_GC_df_filtered=filtered_df["Pourcentage GC"].mean() 
print(f"Pourcentage GC :{average_GC_df_filtered:.3f}%")

#5)Ajouter une nouvelle colonne avec des calculs
print("************* Ajout d'une nouvelle colonne *************")
# Ajouter une nouvelle colonne "catégorisée Pourcentage GC"
df.["Ctégorie Pourcentage GC"]. = df.["Pourcentage GC"].apply(lamba X:"Riche" if X > 55 else ("Moyen" if 45<=55 else
"faible"))

print(df, "\n" "\n")

#6) Ajouter une colonne comptant les 'G'
df.|["Nombre de G"]. = df.["Séquence"].str.count("G")
print("===== Nombre de G ajoutés =====")
print(df, "\n" "\n")

#7)calculer l'écart type du pourcentage GC et de la longueur des séquence
print("*******calcul de l"écart type*******")
écart_type_GC = df["pourcentage GC"].std()
écart_type_longeur = df["longeur"].std()
# print(f"écart typedu pourcentagede GC : {écart_typeGC:.3f}%")
print(f"écart type du longueur:{écart_type_longeur:.3f}%")
# print( "\n" "\n")

#8)sauvegarde et chargement des données avec panda
#sauvegarder le dataframe dans un fichier csv
df.to_csv("tableau_séquence.csv", index=false)