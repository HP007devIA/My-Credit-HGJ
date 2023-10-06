from fastapi import FastAPI
import uvicorn

from pydantic import BaseModel
import pandas as pd
import pickle

# Charger le modèle depuis un fichier Pickle
with open('modele_random_forest.pickle', 'rb') as f:
    modele = pickle.load(f)

# Créez un DataFrame à partir de votre dictionnaire
data_dict = {'age': 30, 'job': 'services', 'marital': 'married', 'education': 'tertiary', 'default': 'no', 'balance': 1350, 'housing': 'yes', 'loan': 'no', 'contact': 'cellular', 'day': 16, 'month': 'oct', 'duration': 185, 'campaign': 1, 'pdays': 330, 'previous': 1, 'poutcome': 'other'}


class Config_donnees(BaseModel):
    age:int
    job:str
    marital:str
    education:str
    default:str
    balance:int
    housing:str
    loan:str
    contact:str
    day:int
    month:str
    duration:int
    campaign:int
    pdays:int
    previous:int
    poutcome:str



app = FastAPI(
    title="Accords Bancaires",
    descrtiption="""
Descritption de l'api ici !!!
"""
)

# Définir une route POST pour la commande
@app.post("/bank_loan")
def predict(data_df: Config_donnees):
    data_df = pd.DataFrame([data_dict])

        # Utilisez le modèle pour effectuer des prédictions
    predictions = modele.predict(data_df)

    # Extrait la valeur de la prédiction (la première prédiction s'il y en a plusieurs)
    prediction = predictions[0]
    return prediction
    """
    Obtenez un avis de prêt bancaire en utilisant les paramètres suivants:
    - **age**:30,
    - **job**:"services",
    - **marital**:"married",
    - **education**:"tertiary",
    - **default**:"no",
    - **balance**:1350,
    - **housing**:"yes",
    - **loan**:"no",
    - **contact**:"cellular",
    - **day**:16,
    - **month**:"oct",
    - **duration**:185,
    - **campaign**:1,
    - **pdays**:330,
    - **previous**:1,
    - **poutcome**:"other"
    ### reponse est égale à 'yes' ou 'no'
    ### proba correspond à la probabilité d'acceptation du dossier
    ### importance est une liste avec une liste des varibales avec la liste du pourcentage d'importance
    """
    transform = functions.scal_lab(n)
    prediction= functions.predictions(transform)
    return prediction

if __name__=='__main__':
    uvicorn.run(app, host='127.0.0.1', port=8001)