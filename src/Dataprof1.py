import pandas as pd
from ydata_profiling import ProfileReport
import time

# import ipywidgets
start_time = time.time()
path1 = '/Users/gerardonunez/Downloads/airline-dataset'
#data = pd.read_parquet( f"{path1}/solicitud.parquet")
#parquet_file = f"{path1}/demo1M.parquet"
data = pd.read_csv( f"{path1}/demo30k.csv")
#data = pd.read_parquet( parquet_file)
# data.to_parquet(parquet_file, index=False)
print(data.head())
data2 = data[["Year","Quarter","Month","DayofMonth","DayOfWeek","FlightDate","Flight_Number_Marketing_Airline","Operating_Airline ","Flight_Number_Operating_Airline","OriginAirportID","OriginAirportSeqID","Origin","OriginState","OriginStateName","DestAirportID","DestAirportSeqID","Dest","DestCityName","DestState","DepDelay","DepDelayMinutes","TaxiOut","TaxiIn","ArrTime","ArrDelay","ArrDelayMinutes","Cancelled","AirTime","WeatherDelay","SecurityDelay"]]


# profile = ProfileReport(data, title="Reporte Datos Solicitud")
# profile.to_file( f"{path1}/flight_data_2018_2024prof.html")

data2.to_csv(f"{path1}/demo30k1.csv")
profile = ProfileReport(data2, title="Reporte Datos Solicitud")
profile.to_file( f"{path1}/data2_profile.html")
end_time = time.time()


print(f"El tiempo de ejecución fue: {end_time - start_time} segundos")



