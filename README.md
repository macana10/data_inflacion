# ETL Inflación Argentina 
El objetivo de este proyecto, es realizar un pequeño ETL de los datos de inflación historico obtenidos a partir de la API del BCRA con el fin de luego exportarlo a un archivo excel .xlsx.

El mismo puede ser utilizados con fines análiticos.

## Instalación

Instalar las dependencias (es decir las librerias necesarias para que se ejecute el archivo .py)

```sh
pip install -r requirements.txt
```

## Obtener token de API del BCRA

Es fundamental obtener el token de la API del BCRA proveniente de este link <https://estadisticasbcra.com/api/documentacion>.
Se registran con su mail y lo obtienen durante 365 días.


## Ejecutar el código

```sh
python inflacion_mes.py
