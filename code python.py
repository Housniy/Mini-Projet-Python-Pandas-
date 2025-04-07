import pandas as pd
import matplotlib.pyplot as plt

# 1. Importation des données
df = pd.read_csv("ventes_laptops.csv")

# 2. Exploration des données
print("Aperçu des données :")
print(df.head())

print("\nInfos générales :")
print(df.info())

print("\nValeurs manquantes :")
print(df.isnull().sum())

# 3. Manipulation des données
# Convertir la colonne 'date' en type datetime
df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y")

# Ajouter une colonne 'mois'
df["mois"] = df["date"].dt.month_name()

# Exemple : filtrer les ventes de plus de 10000€
ventes_hautes = df[df["total"] > 10000]
print("\nVentes > 10000€ :")
print(ventes_hautes)

# Trier par total décroissant
df_sorted = df.sort_values(by="total", ascending=False)

# 4. Analyse statistique
# Calcul des statistiques descriptives : moyenne, médiane, écart-type
moyenne = df[["prix", "quantité", "total"]].mean()
mediane = df[["prix", "quantité", "total"]].median()
ecart_type = df[["prix", "quantité", "total"]].std()

print("\nMoyenne :")
print(moyenne)
print("\nMédiane :")
print(mediane)
print("\nÉcart-type :")
print(ecart_type)

# Ventes totales par mois
ventes_par_mois = df.groupby("mois")["total"].sum().sort_values(ascending=False)
print("\nVentes totales par mois :")
print(ventes_par_mois)

# Moyenne des ventes par produit
moyenne_par_produit = df.groupby("produit")["total"].mean().sort_values(ascending=False)
print("\nMoyenne des ventes par produit :")
print(moyenne_par_produit.head())

# 5. Visualisation des données

# Histogramme des ventes totales
plt.figure(figsize=(10, 5))
plt.hist(df["total"], bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution des montants de ventes")
plt.xlabel("Montant total (€)")
plt.ylabel("Fréquence")
plt.grid(True)
plt.show()

# Courbe des ventes au fil du temps
plt.figure(figsize=(12, 6))
plt.plot(df["date"], df["total"], marker='o', linestyle='-')
plt.title("Évolution des ventes dans le temps")
plt.xlabel("Date")
plt.ylabel("Montant total (€)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Boxplot des prix
plt.figure(figsize=(8, 5))
df.boxplot(column="prix")
plt.title("Répartition des prix des laptops")
plt.ylabel("Prix (€)")
plt.grid(True)
plt.show()
