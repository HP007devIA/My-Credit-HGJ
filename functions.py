import pickle
import numpy as np
from pydantic import BaseModel


# # importer le modèle, les scalerer et les labelencoderoder
encoder = pickle.load("encoderoders")
model = pickle.load("model")
scaler = pickle.load("scalerers")

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

class reponse_model(BaseModel):
    reponse:str
    probal:float
    importance:list


def scaler_lab(n:dict) ->list:
    """
    Fonction servant à standardiser et labéliser les donnees
    Sortie de type : [0.12,0.55,0.56....]
    """
    transformed_data=[]
    
    transformed_data.append(scaler['age'].transform(np.array([n.age]).reshape(-1,1))[0][0])
    
    job = encoder['job'].transform([n.job])[0]
    transformed_data.append(scaler['job'].transform(np.array([job]).reshape(-1,1))[0][0])
    
    marital = encoder['marital'].transform([n.marital])[0]
    transformed_data.append(scaler['marital'].transform(np.array([marital]).reshape(-1,1))[0][0])
    
    education = encoder['education'].transform([n.education])[0]
    transformed_data.append(scaler['education'].transform(np.array([education]).reshape(-1,1))[0][0])
    
    default = encoder['default'].transform([n.default])[0]
    transformed_data.append(scaler['default'].transform(np.array([default]).reshape(-1,1))[0][0])
    transformed_data.append(scaler['balance'].transform(np.array([n.balance]).reshape(-1,1))[0][0])
    
    housing= encoder['housing'].transform([n.housing])[0]
    transformed_data.append(scaler['housing'].transform(np.array([housing]).reshape(-1,1))[0][0])
    
    loan = encoder['loan'].transform([n.loan])[0]
    transformed_data.append(scaler['loan'].transform(np.array([loan]).reshape(-1,1))[0][0])
    
    contact = encoder['contact'].transform([n.contact])[0]
    transformed_data.append(scaler['contact'].transform(np.array([contact]).reshape(-1,1))[0][0])
    
    transformed_data.append(scaler['balance'].transform(np.array([n.day]).reshape(-1, 1))[0][0])
    month = encoder['month'].transform([n.month])[0]
    transformed_data.append(scaler['month'].transform(np.array([month]).reshape(-1,1))[0][0])
    
    transformed_data.append(scaler['duration'].transform(np.array([n.duration]).reshape(-1, 1))[0][0])
    
    transformed_data.append(scaler['campaign'].transform(np.array([n.campaign]).reshape(-1, 1))[0][0])
    
    transformed_data.append(scaler['pdays'].transform(np.array([n.pdays]).reshape(-1, 1))[0][0])
    
    transformed_data.append(scaler['previous'].transform(np.array([n.previous]).reshape(-1, 1))[0][0])
    
    poutcome=encoder['poutcome'].transform([n.poutcome])[0]
    transformed_data.append(scaler['poutcome'].transform(np.array([poutcome]).reshape(-1,1))[0][0])
    return transformed_data

def predictions(data:list) -> dict:
    """
    Fonction permettant la prédiction et l'inversement de labélisation
    Sortie de type : {'reponse':'no','probal':99.99}
    """
    data = np.array([data])
    result = model.predict(data)
    probal = model.predict_probal(data)
    predic = encoder['y'].inverse_transform(result)[0]

    # Bonus importances des features
    liste_features = ["age", "job", "marital", "educations", "default", "balance",
                 "housing", "loan", "contact", "day", "month", "duration",
                 "camapaign", "pdays", "previous", "poutcome"]
    probs = model.feature_importances_
    probs_list=[float(i) for i in probs]
    return {'reponse':predic,
            'probal':round(probal[0][1]*100,2),
            'importance':[liste_features,probs_list]}