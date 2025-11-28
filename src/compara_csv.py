import pandas as pd
import numpy as np


def comparar_archivos_csv(archivo1, archivo2):
    """
    Compara dos archivos CSV y encuentra registros con campos específicos iguales.

    Args:
        archivo1 (str): Ruta del primer archivo CSV
        archivo2 (str): Ruta del segundo archivo CSV

    Returns:
        DataFrame: Registros que coinciden en los campos especificados
    """

    # Campos a comparar
    campos_comparacion = ["ULTIMAUBICACION","FECHAREGISTRO","FECHAREFRENDO","MONTO","DOCUMENTO",
        'NUMERODOCUMENTO',"ASUNTO","AccionRefrendo",
        'FECHAREGISTRO',
        'Codigoarea',
        'Codigoentidad',
        'Codigodependencia',
        'IDEFISCALIZA'
    ]
    campos_comparacion = ["ULTIMAUBICACION","FECHARECEPCION","FECHAREGISTRO","FECHAREFRENDO","CONTROL","IDEFISCALIZA","NUMERODOCUMENTO","MONTO","DOCUMENTO","FLAG_VALOR","SECTOR","DIAS","R1_SV","R2_SV","R3_SV","R4_SV","TIPOORGANIGRAMA","DIRECCION","CODIGOSECTOR","CODIGOOFICINA","CODIGODIRECCION","ASUNTO","EstadoScafid","ASIGNADO","AccionRefrendo","CodigoUsuarioAsignado","Procedencia","Lugar","TipoDocumento","Rango","CodigoDocumento","Codigoarea","Codigoentidad","Codigodependencia","Anio","Afavor","Proveedor","OficinaRegistro","CodigoProcedencia","condicion","FechaModifica","TipoReferencia","SubtipoDocumento","CodigoUltimaUbicacion","Digitalizado","Area","DIASASIGNACION","DIASVIDA","NumeroOrdenacion","RecibidoTN","FechaRecibidoTN","UsuarioRecibidoTN","FechaEntradaCGR","DescripcionFondo","AccionSecretaria","LugarRefrendo","ExpedienteISTMO","UsuarioRegistro","Clasificacion","AccionFiscalizador","TipoFinanciamiento","AnioVigencia","UltimaSecuenciadeSubsanacion","SCAFIDEnlace","DocumentoEnlace","NumeroDocEnlace","AñoDocEnlace","UsuarioRefrendo","UsuarioSubsano","FechaSubsano","NumeroRefrendo","CantidadSubsanacion","DescEstadoScafid","CantidadReingresosporSubsanacion","OFICINATRAMITA"]

    try:
        # Leer los archivos CSV
        print(f"Leyendo {archivo1}...")
        df1 = pd.read_csv(archivo1)

        print(f"Leyendo {archivo2}...")
        df2 = pd.read_csv(archivo2)

        # Verificar que los campos existen en ambos DataFrames
        campos_faltantes_df1 = [campo for campo in campos_comparacion if campo not in df1.columns]
        campos_faltantes_df2 = [campo for campo in campos_comparacion if campo not in df2.columns]

        if campos_faltantes_df1:
            campos_faltantes_df1.to_csv("faltantes1.csv", index=False)
            print(f"Advertencia: Campos faltantes en {archivo1}: {campos_faltantes_df1}")

        if campos_faltantes_df2:
            campos_faltantes_df2.to_csv("faltantes2.csv", index=False)
            print(f"Advertencia: Campos faltantes en {archivo2}: {campos_faltantes_df2}")

        # Solo usar campos que existen en ambos DataFrames
        campos_disponibles = [campo for campo in campos_comparacion
                              if campo in df1.columns and campo in df2.columns]

        if not campos_disponibles:
            print("Error: No hay campos comunes para comparar.")
            return pd.DataFrame()

        print(f"Comparando usando los campos: {campos_disponibles}")

        # Agregar sufijos para identificar el origen de cada DataFrame
        df1_sufijo = df1[campos_disponibles].copy()
        df2_sufijo = df2[campos_disponibles].copy()

        # Realizar merge interno para encontrar coincidencias
        registros_coincidentes = pd.merge(
            df1,
            df2,
            on=campos_disponibles,
            how='inner',
            suffixes=('_f1', '_f2')
        )

        # Mostrar información sobre los resultados
        print(f"\nResultados:")
        print(f"Registros en {archivo1}: {len(df1)}")
        print(f"Registros en {archivo2}: {len(df2)}")
        print(f"Registros con campos coincidentes: {len(registros_coincidentes)}")

        return registros_coincidentes

    except FileNotFoundError as e:
        print(f"Error: No se pudo encontrar el archivo: {e}")
        return pd.DataFrame()

    except pd.errors.EmptyDataError:
        print("Error: Uno de los archivos está vacío.")
        return pd.DataFrame()

    except Exception as e:
        print(f"Error inesperado: {e}")
        return pd.DataFrame()


def mostrar_estadisticas_coincidencias(df_coincidencias, campos_comparacion):
    """
    Muestra estadísticas detalladas sobre las coincidencias encontradas.
    """
    if df_coincidencias.empty:
        print("No se encontraron coincidencias.")
        return

    print(f"\n{'=' * 50}")
    print("ESTADÍSTICAS DETALLADAS")
    print(f"{'=' * 50}")

    # Agrupar por los campos de comparación y contar coincidencias
    for campo in campos_comparacion:
        if campo in df_coincidencias.columns:
            valores_unicos = df_coincidencias[campo].nunique()
            print(f"Valores únicos en {campo}: {valores_unicos}")

    # Mostrar algunas coincidencias como ejemplo
    print(f"\nPrimeras 5 coincidencias encontradas:")
    print("-" * 50)
    print(df_coincidencias.head())


def guardar_resultados(df_coincidencias, archivo_salida="coincidencias.csv"):
    """
    Guarda los resultados en un archivo CSV.
    """
    if not df_coincidencias.empty:
        df_coincidencias.to_csv(archivo_salida, index=False)
        print(f"\nResultados guardados en: {archivo_salida}")
    else:
        print("No hay datos para guardar.")


# Función principal
def main():
    """
    Función principal del script
    """
    path1 = "/Users/gerardonunez/Downloads/DATA-Varios"
    # Nombres de los archivos
    archivo1 = f"{path1}/hechos_pendientes_dias2.csv"
    archivo2 = f"{path1}/Hechos_Pendientes_Dias3.csv"

    print("=" * 60)
    print("COMPARADOR DE ARCHIVOS CSV")
    print("=" * 60)

    # Realizar la comparación
    resultados = comparar_archivos_csv(archivo1, archivo2)

    # Campos que se están comparando
    campos_comparacion = ["ULTIMAUBICACION","FECHAREGISTRO","FECHAREFRENDO","MONTO","DOCUMENTO",
        'NUMERODOCUMENTO',"ASUNTO","AccionRefrendo",
        'FECHAREGISTRO',
        'Codigoarea',
        'Codigoentidad',
        'Codigodependencia',
        'IDEFISCALIZA'
    ]
    campos_comparacion = ["ULTIMAUBICACION", "FECHARECEPCION", "FECHAREGISTRO", "FECHAREFRENDO", "CONTROL",
                          "IDEFISCALIZA", "NUMERODOCUMENTO", "MONTO", "DOCUMENTO", "FLAG_VALOR", "SECTOR", "DIAS",
                          "R1_SV", "R2_SV", "R3_SV", "R4_SV", "TIPOORGANIGRAMA", "DIRECCION", "CODIGOSECTOR",
                          "CODIGOOFICINA", "CODIGODIRECCION", "ASUNTO", "EstadoScafid", "ASIGNADO", "AccionRefrendo",
                          "CodigoUsuarioAsignado", "Procedencia", "Lugar", "TipoDocumento", "Rango", "CodigoDocumento",
                          "Codigoarea", "Codigoentidad", "Codigodependencia", "Anio", "Afavor", "Proveedor",
                          "OficinaRegistro", "CodigoProcedencia", "condicion", "FechaModifica", "TipoReferencia",
                          "SubtipoDocumento", "CodigoUltimaUbicacion", "Digitalizado", "Area", "DIASASIGNACION",
                          "DIASVIDA", "NumeroOrdenacion", "RecibidoTN", "FechaRecibidoTN", "UsuarioRecibidoTN",
                          "FechaEntradaCGR", "DescripcionFondo", "AccionSecretaria", "LugarRefrendo", "ExpedienteISTMO",
                          "UsuarioRegistro", "Clasificacion", "AccionFiscalizador", "TipoFinanciamiento",
                          "AnioVigencia", "UltimaSecuenciadeSubsanacion", "SCAFIDEnlace", "DocumentoEnlace",
                          "NumeroDocEnlace", "AñoDocEnlace", "UsuarioRefrendo", "UsuarioSubsano", "FechaSubsano",
                          "NumeroRefrendo", "CantidadSubsanacion", "DescEstadoScafid",
                          "CantidadReingresosporSubsanacion", "OFICINATRAMITA"]

    # Mostrar estadísticas
    mostrar_estadisticas_coincidencias(resultados, campos_comparacion)

    # Guardar resultados
    if not resultados.empty:
        guardar_resultados(resultados)

        # Opción para mostrar registros duplicados dentro del resultado
        duplicados = resultados.duplicated(subset=campos_comparacion, keep=False)
        if duplicados.any():
            print(f"\nAdvertencia: Se encontraron {duplicados.sum()} registros duplicados en las coincidencias.")

    print(f"\n{'=' * 60}")
    print("PROCESO COMPLETADO")
    print(f"{'=' * 60}")


# Función adicional para análisis más detallado
def analisis_detallado(archivo1, archivo2):
    """
    Realiza un análisis más detallado de las diferencias y similitudes
    """
    campos_comparacion = [
        'NUMERODOCUMENTO',
        'FECHAREGISTRO',
        'Codigoarea',
        'Codigoentidad',
        'Codigodependencia',
        'IDEFISCALIZA'
    ]

    df1 = pd.read_csv(archivo1)
    df2 = pd.read_csv(archivo2)

    print("\nANÁLISIS DETALLADO:")
    print("-" * 40)

    # Registros solo en f1
    solo_f1 = df1.merge(df2, on=campos_comparacion, how='left', indicator=True)
    solo_f1 = solo_f1[solo_f1['_merge'] == 'left_only']
    print(f"Registros solo en {archivo1}: {len(solo_f1)}")

    # Registros solo en f2
    solo_f2 = df2.merge(df1, on=campos_comparacion, how='left', indicator=True)
    solo_f2 = solo_f2[solo_f2['_merge'] == 'left_only']
    print(f"Registros solo en {archivo2}: {len(solo_f2)}")

    return solo_f1, solo_f2


if __name__ == "__main__":
    main()

    # Si quieres ejecutar el análisis detallado, descomenta la siguiente línea:
    # analisis_detallado("f1.csv", "f2.csv")


