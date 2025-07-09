produccion_barriles = 1

if produccion_barriles < 0:
    print("ERROR: no hay producciones negativas")
elif produccion_barriles == 0:
    print("no hubo produccion")
else:
    print("la produccion es ",produccion_barriles)

import os
import pandas as pd

carpeta = "datos"

dataframes = []

for archivo in os.listdir(carpeta) :
    if archivo.endswith(".csv"):
        ruta_completa = os.path.join(carpeta,archivo)
        print(f"Cargando: {archivo}")

        df =pd.read_csv(ruta_completa)
        df['archivo'] = archivo
        print(df.head())
        dataframes.append(df)

#concatenar lista en dataframe

df_final = pd.concat(dataframes, ignore_index=True)

print(df_final.head())

# funcion para calcular el total de barriles
def calcular_total_barriles(df):
    if 'valor' in df.columns:
        return df['valor'].sum()
    else:
        print("La columna 'valor' no existe en el DataFrame.")
        return None
    
print(calcular_total_barriles(df_final))