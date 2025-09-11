import pandas as pd
import sys

import numpy as np
from faker import Faker
import random


# Configurar el generador de datos falsos
fake = Faker('es_ES')  # Usar localización en español
# Faker.seed(56)  # Para reproducibilidad
np.random.seed(56)
random.seed(56)
def generar_lista_con_nan(a, b, x, y, rows):
  """
  Genera una lista de 'rows' números enteros aleatorios entre 'a' y 'b'
  (excluyendo 'b'), reemplazando los valores en el rango [x, y] por NaN.

  Args:
    a (int): Límite inferior (incluido) para la generación de números aleatorios.
    b (int): Límite superior (excluido) para la generación de números aleatorios.
    x (int): Límite inferior (incluido) del rango a reemplazar por NaN.
    y (int): Límite superior (incluido) del rango a reemplazar por NaN.
    rows (int): El número de elementos en la lista a generar.

  Returns:
    numpy.ndarray: Una lista de números aleatorios con NaNs.
  """
  # 1. Generar el array de números enteros aleatorios
  lista_aleatoria = np.random.randint(a, b, size=rows)

  # 2. Crear una máscara booleana para los valores en el rango [x, y]
 # mascara_nan = (lista_aleatoria >= x) & (lista_aleatoria <= y)
  lista = lista_aleatoria.tolist()
  for i in range(len(lista)):
      if lista[i] >  x and lista[i]  < y:
          lista[i] = np.nan


  # 3. Reemplazar los valores que cumplen la condición con NaN
  #lista_aleatoria[mascara_nan] = np.nan

  return lista

def gen_cedula():
    prov = [1,2,3,3,3,3,4,4,4,4,5,5,5,6,7,8,8,8,9,10,"PE","N"]
    idx =  fake.random_int(min=0, max=len(prov)-1 )
    dig2 = fake.random_int(min=100, max=999 )
    dig3 = fake.random_int(min=1000, max=9999 )
    cedula = f"{str(prov[idx])}-{dig2}-{dig3}"
    return cedula

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
        'edad': generar_lista_con_nan(18,80,20,25,num_filas),
        #np.random.randint(18, 80, num_filas),
        'salario': np.random.normal(50000, 15000, num_filas).round(2),
        'puntuacion': np.random.uniform(0, 10, num_filas).round(2),
        'cantidad': np.random.poisson(5, num_filas),
        'precio': np.random.exponential(25, num_filas).round(2),

        # Columnas de texto usando Faker
        'nombre': [fake.name() for _ in range(num_filas)],
        'cedula': [gen_cedula() for _ in range(num_filas)],
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
    # for i in range(100):
    #   print(gen_cedula())
    # Crear el DataFrame
    NUM_FILAS = 8_000_000
    df = crear_dataframe_aleatorio(num_filas=NUM_FILAS)

    # Mostrar información
    mostrar_informacion_dataframe(df)

    # Guardar en archivo CSV (opcional)
    path1= "/Users/gerardonunez/Downloads/DATA-seminario"
    archivo_csv =  f"{path1}/demo8M.csv"

    df.to_csv(archivo_csv, index=False)

    print(f"✅ Conversión exitosa:")

    print(f"\n✅ Datos guardados en archivo_csv:'{archivo_csv}'")

    # Algunos ejemplos de análisis básico

    print("ANÁLISIS BÁSICO")
    print("=" * 50)

    print(f"Edad promedio: {df['edad'].mean():.1f} años")
    print(f"Salario promedio: ${df['salario'].mean():.2f}")
    print(f"Distribución por categoría:")
    print(df['categoria'].value_counts())
    print(f"\nDistribución por estado:")
    print(df['estado'].value_counts())
    duplicados = df['cedula'].duplicated()
    print(f"Cedulas Duplicadas: {duplicados}")

    # Filtrar algunos ejemplos
    print(f"\nPersonas mayores de 50 años: {len(df[df['edad'] > 50])}")
    print(f"Personas con salario > $60,000: {len(df[df['salario'] > 60000])}")
