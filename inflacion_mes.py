import requests
import pandas as pd

def extract(url: str, headers: dict):
    """
    Función para extraer datos de una API utilizando la librería requests.
    """
    respuesta = requests.get(url, headers=headers)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        return datos
    else:
        print(f"Error al hacer la consulta. Código de estado: {respuesta.status_code}")

def transform(datos: dict):
    """
    Función para transformar los datos obtenidos en formato JSON a un DataFrame de Pandas.
    """
    df = pd.DataFrame(datos)
    df = df.rename(columns={'d': 'fecha', 'v': 'valor'})
    df['fecha'] = pd.to_datetime(df['fecha'])
    return df

def load(df: pd.DataFrame, file_path: str):
    """
    Función para cargar los datos en un archivo Excel.
    """
    df.to_excel(file_path, sheet_name='inflacion_mensual', index=False)

def main():
    # URL de la API del BCRA para obtener datos de inflación
    api_url = "https://api.estadisticasbcra.com/"
    token = "COLOCAR EL TOKEN"

    # Creamos el encabezado con el token de acceso
    headers = {
        'Authorization': 'BEARER ' + token
    }

    # Definimos los indicadores que queremos obtener
    indicadores = {
        'inflacion_mensual_oficial': None
    }

    # Iteramos sobre los indicadores y hacemos la consulta a la API
    for nombre, endpoint in indicadores.items():
        url = api_url + nombre
        datos = extract(url, headers)
        if datos is not None:
            df = transform(datos)
            load(df, 'inflacion_mensual.xlsx')

if __name__ == "__main__":
    main()
