import joblib
import os

def cargar_modelos():
    modelos = {}
    try:
        # Obtiene el directorio donde *está* este script (cargar_modelos.py)
        models_dir = os.path.dirname(os.path.abspath(__file__))

        modelos = {
            "modelo1": joblib.load(os.path.join(models_dir, "modelo1.pkl")),
            "modelo2": joblib.load(os.path.join(models_dir, "modelo2.pkl")),
            "modelo3": joblib.load(os.path.join(models_dir, "modelo3.pkl")),
            "modelo4": joblib.load(os.path.join(models_dir, "modelo4.pkl")),
            "column_order": joblib.load(os.path.join(models_dir, "column_order.pkl")),
        }
        return modelos
    except FileNotFoundError:
        print(f"Error: No se encontraron los archivos .pkl en la carpeta models: {os.path.join(models_dir, 'modelo1.pkl')}")
        return None
    except Exception as e:
        print(f"Error al cargar los modelos: {e}")
        return None