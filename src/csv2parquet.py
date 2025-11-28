import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import os
import sys


def csv_to_parquet_basic(csv_file, parquet_file):
    """
    Convierte un archivo CSV a Parquet usando pandas y pyarrow

    Args:
        csv_file (str): Ruta del archivo CSV de entrada
        parquet_file (str): Ruta del archivo Parquet de salida
    """
    try:
        # Leer el archivo CSV
        print(f"Leyendo archivo CSV: {csv_file}")
        df = pd.read_csv(csv_file)

        # Mostrar información básica
        print(f"Filas: {len(df)}, Columnas: {len(df.columns)}")
        print(f"Columnas: {list(df.columns)}")

        # Guardar como Parquet
        print(f"Guardando archivo Parquet: {parquet_file}")
        df.to_parquet(parquet_file, engine='pyarrow', index=False)

        print("¡Conversión completada exitosamente!")

    except Exception as e:
        print(f"Error durante la conversión: {str(e)}")


# Ejemplo de uso
if __name__ == "__main__":
    path = "/Users/gerardonunez/Downloads/DATA-seminario"
    csv_file = f"{path}/demo1M.csv"
    parquet_file = f"{path}/demo1M.parquet"
    csv_to_parquet_basic(csv_file, parquet_file)