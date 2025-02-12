import numpy as np 
import pandas as pd 
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC  # Máquinas de Vectores de Soporte (clasificación)
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier  # Perceptrón Multicapa (clasificación)
from sklearn.neighbors import KNeighborsClassifier
import pickle
import os

#cargadataset
current_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(current_dir, "data", "penguins_size.csv"))
#limpesa y tranfomracion feactures categoricoa 
df.dropna(inplace=True)  # Eliminar filas con valores faltantes (opción simple para este dataset)
df = pd.get_dummies(df, columns=[ 'island', 'sex'], drop_first=True)

#separa data set en mi feactures y mi variable objetvo
X = df.drop('species', axis=1)   # Variable objetivo: body_mass_g
y = df['species'] 

#particona  data set en datos de entrenamineto y de prueba

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
column_order = X_train.columns
with open(os.path.join(current_dir, "models", "column_order.pkl"), "wb") as f:
    pickle.dump(column_order, f)
#INICA ENTRENAMIENTO DE MODELOS 
model1= KNeighborsClassifier(n_neighbors=5)  # Ajusta n_neighbors (número de vecinos)
model1.fit(X_train, y_train)

# Modelo 2: Máquina de Vectores de Soporte
model2 = SVC()
model2.fit(X_train, y_train)

model3 = GaussianNB()  # Para datos numéricos continuos
model3.fit(X_train, y_train)

# Modelo 4: Perceptrón Multicapa
model4 = MLPClassifier(max_iter=1000)  # Aumenta max_iter si es necesario
model4.fit(X_train, y_train)

#evalua modelos 
y_pred1 = model1.predict(X_test)
y_pred2 = model2.predict(X_test)
y_pred3 = model3.predict(X_test)
y_pred4 = model4.predict(X_test)

accuracy_modelo1 = accuracy_score(y_test, y_pred1)

print(f"Accuracy Modelo 1: {accuracy_modelo1}")

accuracy_modelo2 = accuracy_score(y_test, y_pred2)
print(f"Accuracy Modelo 2: {accuracy_modelo2}")

accuracy_modelo3 = accuracy_score(y_test, y_pred3)
print(f"Accuracy Modelo 3: {accuracy_modelo3}")

accuracy_modelo4 = accuracy_score(y_test, y_pred4)
print(f"Accuracy Modelo 4: {accuracy_modelo4}")

joblib.dump(model1, os.path.join(current_dir, "models", "modelo1.pkl"))
joblib.dump(model2, os.path.join(current_dir, "models", "modelo2.pkl"))
joblib.dump(model3, os.path.join(current_dir, "models", "modelo3.pkl"))
joblib.dump(model4, os.path.join(current_dir, "models", "modelo4.pkl"))