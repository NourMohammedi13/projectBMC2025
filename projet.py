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

#3) filtrer les séquences avec une longuer superieur à 10
print("************fltrage avec longuer >10*************")
filtered_df=df[df["longuer"]>10]
print(filtered_df)

#4) la moyenne de pourcentage GC
print("**************moyenne de pourcentage GC%**************")
average_GC=df["pourcentage GC"].mean() 
print(f"pourcentage GC :{averae_GC:.3f}")

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