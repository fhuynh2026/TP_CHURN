import pandas as pd
import numpy as np 
from sklearn.linear_model import LogisticRegression
import joblib    

# charger les données      

data = pd.read_csv('data/customer_churn.csv')

x= data[['Age', 'Account_Manager', 'Years', 'Num_Sites']]

#selectionner la colonne cible

y = data['Churn']

#creer et entrainer le modele de regression logistique

model = LogisticRegression()

# entrainer le modele sur les données

model.fit(x,y)

# sauvegarder le modele entrainé avec joblib (sans dependances par joblib.dump)
joblib.dump(model, 'data/churn_model_clean.pkl')

print("Modele de regresionn logistique entrainé et sauveardé")
