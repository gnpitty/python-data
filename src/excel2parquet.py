import pandas as pd
import sys

import numpy as np
from faker import Faker
import random
from ydata_profiling import ProfileReport

def excel_to_parquet(excel_file, parquet_file=None):
    """
    Convierte un archivo Excel a formato Parquet

    Args:
        excel_file (str): Ruta del archivo Excel
        parquet_file (str): Ruta del archivo Parquet (opcional)
    """
    try:
        # Leer el archivo Excel
        df = pd.read_excel(excel_file)

        # Si no se especifica nombre de salida, usar el mismo nombre con extensión .parquet
        if parquet_file is None:
            parquet_file = excel_file.rsplit('.', 1)[0] + '.parquet'

        # Guardar como parquet
        df.to_parquet(parquet_file, index=False)
        #table = pa.Table.from_pandas(df)

        print(f"✅ Conversión exitosa:")
        print(f"   📁 Origen: {excel_file}")
        print(f"   📁 Destino: {parquet_file}")
        print(f"   📊 Filas: {len(df)}, Columnas: {len(df.columns)}")

    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo {excel_file}")
    except Exception as e:
        print(f"❌ Error durante la conversión: {str(e)}")




# Configurar el generador de datos falsos
fake = Faker('es_ES')  # Usar localización en español
Faker.seed(56)  # Para reproducibilidad
np.random.seed(56)
random.seed(56)


def crear_dataframe_aleatorio(num_filas=100):
    """
    Crea un DataFrame con columnas numéricas aleatorias y columnas de texto faker

    Args:
        num_filas (int): Número de filas a generar

    Returns:
        pd.DataFrame: DataFrame con datos aleatorios
    """

    data = {
        # Columnas numéricas con diferentes distribuciones
        'id': range(1, num_filas + 1),
        'edad': np.random.randint(18, 80, num_filas),
        'salario': np.random.normal(50000, 15000, num_filas).round(2),
        'puntuacion': np.random.uniform(0, 10, num_filas).round(2),
        'cantidad': np.random.poisson(5, num_filas),
        'precio': np.random.exponential(25, num_filas).round(2),

        # Columnas de texto usando Faker
        'nombre': [fake.name() for _ in range(num_filas)],
        'email': [fake.email() for _ in range(num_filas)],
        'ciudad': [fake.city() for _ in range(num_filas)],
        'empresa': [fake.company() for _ in range(num_filas)],
        'telefono': [fake.phone_number() for _ in range(num_filas)],
        'direccion': [fake.address().replace('\n', ', ') for _ in range(num_filas)],
        'fecha_nacimiento': [fake.date_of_birth(minimum_age=18, maximum_age=80) for _ in range(num_filas)],
        'profesion': [fake.job() for _ in range(num_filas)],
        'descripcion': [fake.text(max_nb_chars=100) for _ in range(num_filas)],

        # Columnas categóricas aleatorias
        'categoria': np.random.choice(['A', 'B', 'C', 'D'], num_filas),
        'estado': np.random.choice(['Activo', 'Inactivo', 'Pendiente'], num_filas),
        'genero': np.random.choice(['M', 'F'], num_filas)
    }

    df = pd.DataFrame(data)

    # Asegurar que los salarios sean positivos
    df['salario'] = df['salario'].abs()

    return df


def mostrar_informacion_dataframe(df):
    """
    Muestra información básica del DataFrame
    """
    print("=" * 50)
    print("INFORMACIÓN DEL DATAFRAME")
    print("=" * 50)
    print(f"Dimensiones: {df.shape}")
    print(f"Columnas: {list(df.columns)}")
    print("\nTipos de datos:")
    print(df.dtypes)
    print("\nPrimeras 5 filas:")
    print(df.head())
    print("\nEstadísticas descriptivas (columnas numéricas):")
    print(df.describe())


# Script principal
if __name__ == "__main__":
    print("Generando DataFrame con datos aleatorios...")

    # Crear el DataFrame
    df = crear_dataframe_aleatorio(num_filas=800)

    # Mostrar información
    mostrar_informacion_dataframe(df)

    # Guardar en archivo CSV (opcional)
    path1= "/Users/gerardonunez/Downloads/DATA-seminario"
    archivo_excel = f"{path1}/demo.xlsx"
    archivo_csv =  f"{path1}/demo.csv"
    parquet_file = f"{path1}/demo.parquet"

        # Guardar como parquet
    df.to_parquet(parquet_file, index=False)
    df.to_csv(archivo_csv, index=False)

    df.to_excel(archivo_excel, index=False, sheet_name='Sheet1')
    print(f"✅ Conversión exitosa:")

    print(f"   📁 Destino: {parquet_file}")

    df.to_csv(archivo_csv, index=False, encoding='utf-8')
    print(f"\n✅ Datos guardados en archivo_csv:'{archivo_csv}'")

    # Algunos ejemplos de análisis básico
    print("\n" + "=" * 50)
    print("ANÁLISIS BÁSICO")
    print("=" * 50)

    print(f"Edad promedio: {df['edad'].mean():.1f} años")
    print(f"Salario promedio: ${df['salario'].mean():.2f}")
    print(f"Distribución por categoría:")
    print(df['categoria'].value_counts())
    print(f"\nDistribución por estado:")
    print(df['estado'].value_counts())

    # Filtrar algunos ejemplos
    print(f"\nPersonas mayores de 50 años: {len(df[df['edad'] > 50])}")
    print(f"Personas con salario > $60,000: {len(df[df['salario'] > 60000])}")




    profile = ProfileReport(df, title="Profiling Report")
    profile.to_file(f"{path1}/profiling_report.html")

    # excel_to_parquet("/Users/gerardonunez/Downloads/cliente.xlsx", "cliente.parquet")