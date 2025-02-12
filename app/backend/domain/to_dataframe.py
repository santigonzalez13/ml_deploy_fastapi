import pandas as pd


def to_dataframe(pinguino):
        columnas_base = ['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g', 'island_Dream', 'island_Torgersen', 'sex_FEMALE', 'sex_MALE']
        data = {
            'culmen_length_mm': [pinguino.culmen_length_mm],
            'culmen_depth_mm': [pinguino.culmen_depth_mm],
            'flipper_length_mm': [pinguino.flipper_length_mm],
            'island': [pinguino.island],
            'sex': [pinguino.sex],
            'body_mass_g': [pinguino.body_mass_g]
        }
        df = pd.DataFrame(data)

        # 1. Crear un DataFrame *vacío* con las columnas base
        df_nuevo = pd.DataFrame(columns=columnas_base)

        # 2. Asignar los valores del pingüino al DataFrame vacío
        df_nuevo[['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g']] = df[['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g']].values
        
        # 3. Crear las columnas dummy *manualmente*
        if pinguino.island == 'Dream':
            df_nuevo['island_Dream'] = 1
            df_nuevo['island_Torgersen'] = 0
        elif pinguino.island == 'Torgersen':
            df_nuevo['island_Torgersen'] = 1
            df_nuevo['island_Dream'] = 0
        # Si la isla es 'Biscoe' (u otra), las columnas dummy correspondientes ya están a 0 por defecto

        if pinguino.sex == 'FEMALE':
            df_nuevo['sex_FEMALE'] = 1
            df_nuevo['sex_MALE'] = 0
        elif pinguino.sex == 'MALE':
            df_nuevo['sex_MALE'] = 1
            df_nuevo['sex_FEMALE'] = 0
        # Si el sexo es 'Unknown' (u otro), las columnas dummy correspondientes ya están a 0 por defecto

        return df_nuevo