import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import os
from typing import Optional


def csv_to_parquet_chunks(csv_file: str, parquet_file: str,
                          chunk_size: int = 100000,
                          compression: str = 'snappy'):
    """
    Convierte un archivo CSV grande a Parquet procesando en chunks

    Args:
        csv_file (str): Ruta del archivo CSV de entrada
        parquet_file (str): Ruta del archivo Parquet de salida
        chunk_size (int): Número de filas por chunk
        compression (str): Tipo de compresión
    """

    writer = None
    schema = None
    total_rows = 0

    try:
        print(f"Procesando archivo en chunks de {chunk_size:,} filas")

        # Procesar archivo en chunks
        for chunk_num, chunk_df in enumerate(pd.read_csv(csv_file, chunksize=chunk_size)):
            print(f"Procesando chunk {chunk_num + 1}: {len(chunk_df):,} filas")

            # Convertir chunk a tabla Arrow
            table = pa.Table.from_pandas(chunk_df)

            # Inicializar writer con el primer chunk
            if writer is None:
                schema = table.schema
                writer = pq.ParquetWriter(parquet_file, schema, compression=compression)

            # Escribir chunk
            writer.write_table(table)
            total_rows += len(chunk_df)

        # Cerrar writer
        if writer:
            writer.close()

        print(f"\nConversión completada:")
        print(f"- Total de filas procesadas: {total_rows:,}")
        print(f"- Archivo guardado: {parquet_file}")

        # Mostrar estadísticas del archivo
        file_size = os.path.getsize(parquet_file) / 1024 ** 2
        print(f"- Tamaño final: {file_size:.2f} MB")

    except Exception as e:
        if writer:
            writer.close()
        print(f"Error durante la conversión: {str(e)}")
        # Limpiar archivo parcial en caso de error
        if os.path.exists(parquet_file):
            os.remove(parquet_file)


# Ejemplo de uso
if __name__ == "__main__":
    # Para archivos grandes
    path = "/Users/gerardonunez/Downloads/DATA-seminario"
    csv_file = f"{path}/demo1M.csv"
    parquet_file = f"{path}/demo1M_A.parquet"
    csv_to_parquet_chunks(
        csv_file=csv_file,
        parquet_file=parquet_file,
        chunk_size=200000,
        compression='snappy'
    )