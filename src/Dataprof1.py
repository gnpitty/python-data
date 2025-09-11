import pandas as pd
from ydata_profiling import ProfileReport
import time

import ipywidgets
start_time = time.time()
path1 = '/tmp'
#data = pd.read_parquet( f"{path1}/solicitud.parquet")
parquet_file = f"{path1}/demo1M.parquet"
#data = pd.read_csv( f"{path1}/demo1M.csv")
data = pd.read_parquet( parquet_file)
# data.to_parquet(parquet_file, index=False)
print(data.head())


profile = ProfileReport(data, title="Reporte Datos Solicitud")
profile.to_file( f"{path1}/demo1M_prof.html")
end_time = time.time()

print(f"El tiempo de ejecución fue: {end_time - start_time} segundos")



