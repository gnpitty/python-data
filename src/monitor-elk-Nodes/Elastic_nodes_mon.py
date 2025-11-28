import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import argparse
import sys
import os


class MonitoringPlotter:
    def __init__(self):
        """Inicializa el graficador de monitoreo"""
        plt.style.use('default')
        self.colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

    def read_csv_file(self, filepath, node_name=None):
        """
        Lee un archivo CSV y procesa las columnas de fecha y hora

        Args:
            filepath (str): Ruta del archivo CSV
            node_name (str): Nombre del nodo (opcional)

        Returns:
            pd.DataFrame: DataFrame con los datos procesados
        """
        try:
            # Leer el archivo CSV
            df = pd.read_csv(filepath)

            # Verificar que las columnas requeridas existan
            required_columns = ['Fecha', 'Hora', 'CPU_Porcentaje', 'Memoria_Porcentaje',
                                'SWAP_Porcentaje', 'CPU_MB', 'Memoria_Total_MB', 'Memoria_Usada_MB']

            missing_columns = [col for col in required_columns if col not in df.columns]
            if missing_columns:
                raise ValueError(f"Columnas faltantes en {filepath}: {missing_columns}")

            # Combinar fecha y hora en una sola columna datetime
            df['DateTime'] = pd.to_datetime(df['Fecha'] + ' ' + df['Hora'])

            # Ordenar por fecha/hora
            df = df.sort_values('DateTime')

            # Agregar nombre del nodo si se proporciona
            if node_name:
                df['Nodo'] = node_name

            print(f"✓ Archivo leído exitosamente: {filepath}")
            print(f"  - Registros: {len(df)}")
            print(f"  - Rango de fechas: {df['DateTime'].min()} a {df['DateTime'].max()}")

            return df

        except Exception as e:
            print(f"✗ Error al leer {filepath}: {str(e)}")
            return None

    def plot_single_node(self, df, node_name, save_path=None):
        """
        Crea gráficas para un solo nodo

        Args:
            df (pd.DataFrame): DataFrame con los datos
            node_name (str): Nombre del nodo
            save_path (str): Ruta para guardar la imagen (opcional)
        """
        fig, (ax1) = plt.subplots(1, 1, figsize=(12, 10))

        # Gráfica 1: CPU y Memoria Porcentaje
        ax1.plot(df['DateTime'], df['CPU_Porcentaje'],
                 label='CPU %', color=self.colors[0], linewidth=2)
        ax1.plot(df['DateTime'], df['Memoria_Porcentaje'],
                 label='Memoria %', color=self.colors[1], linewidth=2)



        ax1.set_title(f'{node_name} - CPU y Memoria (%)', fontsize=14, fontweight='bold')
        ax1.set_ylabel('Porcentaje (%)')
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        ax1.set_ylim(0, 100)

        # Formatear eje x
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
        ax1.xaxis.set_major_locator(mdates.HourLocator(interval=12))
        # ax1.xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Un tick por día
        # ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Form

        plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)

        # # Gráfica 2: SWAP Porcentaje
        # ax2.plot(df['DateTime'], df['SWAP_Porcentaje'],
        #          label='SWAP %', color=self.colors[2], linewidth=2)
        #
        # ax2.set_title(f'{node_name} - SWAP (%)', fontsize=14, fontweight='bold')
        # ax2.set_xlabel('Fecha y Hora')
        # ax2.set_ylabel('Porcentaje (%)')
        # ax2.grid(True, alpha=0.3)
        # ax2.legend()
        # ax2.set_ylim(0, max(100, df['SWAP_Porcentaje'].max() * 1.1))

        # Formatear eje x
        # ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
        # ax2.xaxis.set_major_locator(mdates.HourLocator(interval=1))
        # plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)

        plt.tight_layout()

        if save_path:
            plt.savefig(f"{save_path}/{node_name}_individual.png", dpi=300, bbox_inches='tight')
            print(f"✓ Gráfica guardada: {save_path}_{node_name}_individual.png")

        plt.show()

    def plot_comparison(self, df1, df2, node1_name, node2_name, save_path=None):
        """
        Crea gráficas comparativas entre dos nodos

        Args:
            df1, df2 (pd.DataFrame): DataFrames con los datos de cada nodo
            node1_name, node2_name (str): Nombres de los nodos
            save_path (str): Ruta para guardar la imagen (opcional)
        """
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 12))

        # Gráfica 1: CPU Comparación
        ax1.plot(df1['DateTime'], df1['CPU_Porcentaje'],
                 label=f'{node1_name} - CPU %', color=self.colors[0], linewidth=2)
        ax1.plot(df2['DateTime'], df2['CPU_Porcentaje'],
                 label=f'{node2_name} - CPU %', color=self.colors[1], linewidth=2)

        ax1.set_title('Comparación CPU (%)', fontsize=14, fontweight='bold')
        ax1.set_ylabel('CPU Porcentaje (%)')
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        ax1.set_ylim(0, 100)

        # Gráfica 2: Memoria Comparación
        ax2.plot(df1['DateTime'], df1['Memoria_Porcentaje'],
                 label=f'{node1_name} - Memoria %', color=self.colors[2], linewidth=2)
        ax2.plot(df2['DateTime'], df2['Memoria_Porcentaje'],
                 label=f'{node2_name} - Memoria %', color=self.colors[3], linewidth=2)

        ax2.set_title('Comparación Memoria (%)', fontsize=14, fontweight='bold')
        ax2.set_ylabel('Memoria Porcentaje (%)')
        ax2.grid(True, alpha=0.3)
        ax2.legend()
        ax2.set_ylim(0, 100)

        # Gráfica 3: SWAP Comparación
        ax3.plot(df1['DateTime'], df1['SWAP_Porcentaje'],
                 label=f'{node1_name} - SWAP %', color=self.colors[4], linewidth=2)
        ax3.plot(df2['DateTime'], df2['SWAP_Porcentaje'],
                 label=f'{node2_name} - SWAP %', color=self.colors[5], linewidth=2)

        ax3.set_title('Comparación SWAP (%)', fontsize=14, fontweight='bold')
        ax3.set_xlabel('Fecha y Hora')
        ax3.set_ylabel('SWAP Porcentaje (%)')
        ax3.grid(True, alpha=0.3)
        ax3.legend()

        # Establecer límite del eje Y para SWAP
        max_swap = max(df1['SWAP_Porcentaje'].max(), df2['SWAP_Porcentaje'].max())
        ax3.set_ylim(0, max(100, max_swap * 1.1))

        # Formatear ejes x para todas las gráficas
        for ax in [ax1, ax2, ax3]:
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
            ax.xaxis.set_major_locator(mdates.HourLocator(interval=8))
            plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)

        plt.tight_layout()

        if save_path:
            plt.savefig(f"{save_path}/comparison.png", dpi=300, bbox_inches='tight')
            print(f"✓ Gráfica de comparación guardada: {save_path}_comparison.png")

        plt.show()

    def generate_summary_stats(self, df, node_name):
        """
        Genera estadísticas resumidas de los datos

        Args:
            df (pd.DataFrame): DataFrame con los datos
            node_name (str): Nombre del nodo
        """
        print(f"\n=== Estadísticas Resumidas - {node_name} ===")

        metrics = ['CPU_Porcentaje', 'Memoria_Porcentaje', 'SWAP_Porcentaje']

        for metric in metrics:
            print(f"\n{metric}:")
            print(f"  Promedio: {df[metric].mean():.2f}%")
            print(f"  Mínimo: {df[metric].min():.2f}%")
            print(f"  Máximo: {df[metric].max():.2f}%")
            print(f"  Desv. Estándar: {df[metric].std():.2f}%")


def main():
    """Función principal del script"""
    # parser = argparse.ArgumentParser(description='Graficador de métricas de monitoreo de sistemas')

    # parser.add_argument('--save', help='Ruta base para guardar las gráficas')
    # parser.add_argument('--stats', action='store_true', help='Mostrar estadísticas resumidas')


    path = "/Users/gerardonunez/DATA-Elastic"
    file1 = f"{path}/system_monitor.csv"
    file2 = f"{path}/system_monitor03.csv"
    node1 = "cgrbi04"
    node2 = "cgrbi03"



    # Crear instancia del graficador
    plotter = MonitoringPlotter()

    # Leer el primer archivo
    print("Leyendo archivos...")
    df1 = plotter.read_csv_file(file1, node1)

    if df1 is None:
        sys.exit(1)

    # Generar estadísticas si se solicita
    plotter.generate_summary_stats(df1, node1)

    # Generar gráfica individual del primer nodo
    print(f"\nGenerando gráficas para {node1}...")
    plotter.plot_single_node(df1, node1, path)

    # Si hay un segundo archivo, procesarlo también
    if file2:
        df2 = plotter.read_csv_file(file2, node2)

        if df2 is not None:
            # Generar estadísticas del segundo nodo si se solicita
            
            plotter.generate_summary_stats(df2, node2)

            # Generar gráfica individual del segundo nodo
            print(f"\nGenerando gráficas para {node2}...")
            plotter.plot_single_node(df2, node2, path)

            # Generar gráfica comparativa
            print(f"\nGenerando gráficas comparativas...")
            plotter.plot_comparison(df1, df2, node1, node2, path)
        else:
            print("✗ No se pudo procesar el segundo archivo")

    print("\n✓ Proceso completado exitosamente")


if __name__ == "__main__":
    main()