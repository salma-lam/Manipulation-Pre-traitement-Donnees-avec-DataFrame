import pandas as pd # Charger le dataset depuis un fichier CSV
df = pd.read_csv('TP-01-Dataset.csv') 
# Afficher les 5 premières lignes
 print(df.head()) 
# Afficher les 5 dernières lignes
 print(df.tail())
# Afficher les informations générales sur le DataFrame 
 print(df.info())
# Résumé statistique des colonnes numériques
 print(df.describe())