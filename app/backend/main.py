from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from domain.to_dataframe import to_dataframe
from models.cargar_modelos import cargar_modelos
from collections import Counter

app = FastAPI()

class Pinguino(BaseModel):
    culmen_length_mm: float
    culmen_depth_mm: float
    flipper_length_mm: float
    body_mass_g: float
    island: str
    sex: str
    
modelos_name = {
    "modelo1": "KNeighborsClassifier",
    "modelo2": "SVC",
    "modelo3": "GaussianNB",
    "modelo4": "MLPClassifier"
}

@app.post("/pinguino")
def postPinguino(pinguino: Pinguino):
    print("iciaa")
    df = to_dataframe(pinguino)# tranforma mi calse pinguino en un dataframe como el que se uso para entenerar los modelos
    modelos= cargar_modelos()# carga los modelos entreandos
    print(modelos)
    df = df[ modelos['column_order']]# define el orden de las columnas igual a las del modelo entrenado
    listaInferencia = [modelos[f'modelo{i}'].predict(df).tolist()[0] for i in range(1, 5)]#crea una lista de los modelos 
    # Función lambda para encontrar el elemento más frecuente (directamente en la línea)
    elemento_mas_frecuente = lambda lista: (lambda c: (lambda: c.most_common(1)[0][0])() if c else None)(Counter(lista))
    elemento_mas_comun = elemento_mas_frecuente(listaInferencia)
    print(elemento_mas_comun)
    return {"message": "Pinguino recibido", "data": elemento_mas_comun}


@app.post("/pinguino/{modelo}")
def postPinguino(pinguino: Pinguino, modelo:str):
    print("inicia")
    print( modelos_name[modelo])
    df = to_dataframe(pinguino)# tranforma mi calse pinguino en un dataframe como el que se uso para entenerar los modelos
    modelos= cargar_modelos()# carga los modelos entreandos
    print(type(modelos))
    print(modelos)
    df = df[ modelos['column_order']]# define el orden de las columnas igual a las del modelo entrenado
    
    inferencia = modelos[modelo].predict(df)    
    print("data :", inferencia)
    return {"Modelo Usado ": modelos_name[modelo], "Inferencia":   inferencia[0]}

