import pandas as pd
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def leer_datos_csv():
    source = os.path.join(BASE_DIR, "Titanic.csv")
    df=pd.read_csv(source)
    print(f'total lineas importadas:  {len(df)}')
    return df