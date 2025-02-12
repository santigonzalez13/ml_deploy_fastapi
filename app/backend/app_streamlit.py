import streamlit as st
import requests
import pandas as pd

# URL de tu API FastAPI
API_URL = "http://127.0.0.1:8989/pinguino"  # Reemplaza con tu URL real

# Diccionario de modelos para Streamlit (value: nombre para mostrar, key: nombre para la API)
MODELOS = {
    "K-Nearest Neighbors": "modelo1",
    "Support Vector Machine": "modelo2",
    "Naive Bayes": "modelo3",
    "Perceptrón Multicapa": "modelo4",
}

st.title("Predicción de Pingüino")

with st.form("pinguino_form"):
    # Selector de modelo
    modelo_seleccionado = st.selectbox("Selecciona el modelo", list(MODELOS.keys()))

    # Datos del pingüino
    culmen_length_mm = st.number_input("Culmen Length (mm)", min_value=0.0)
    culmen_depth_mm = st.number_input("Culmen Depth (mm)", min_value=0.0)
    flipper_length_mm = st.number_input("Flipper Length (mm)", min_value=0.0)
    body_mass_g = st.number_input("Body Mass (g)", min_value=0)
    island = st.selectbox("Island", ["Torgersen", "Dream"])
    sex = st.selectbox("Sex", ["MALE", "FEMALE"])

    submitted = st.form_submit_button("Predecir")

if submitted:
    # Obtener el nombre del modelo para la API
    modelo_api = MODELOS[modelo_seleccionado]

    # Datos del pingüino
    pinguino_data = {
        "culmen_length_mm": culmen_length_mm,
        "culmen_depth_mm": culmen_depth_mm,
        "flipper_length_mm": flipper_length_mm,
        "body_mass_g": body_mass_g,
        "island": island,
        "sex": sex,
    }

    try:
        # Enviar petición POST a la API con el modelo seleccionado
        response = requests.post(f"{API_URL}/{modelo_api}", json=pinguino_data)

        # Manejar la respuesta
        if response.status_code == 200:
            prediction = response.json()
            st.success(f"Modelo Usado: {prediction['Modelo Usado ']}\nPredicción: {prediction['Inferencia']}")
        else:
            st.error(f"Error en la API: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        st.error(f"Error de conexión: {e}")

    # Tabla de datos (opcional)
    data = {'culmen_length_mm': [culmen_length_mm], 'culmen_depth_mm': [culmen_depth_mm],
            'flipper_length_mm': [flipper_length_mm], 'body_mass_g': [body_mass_g],
            'island': [island], 'sex': [sex], 'modelo': [modelo_seleccionado]}
    df = pd.DataFrame(data)
    st.write("Datos ingresados:")
    st.dataframe(df)