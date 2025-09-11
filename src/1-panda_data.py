import pandas as pd
import numpy as np
import datetime
# Generate dataset
rows = 10_000_000
# np.random.seed(42)
# data = {
#     'id': np.arange(rows),
#     'name': np.random.choice(['Juan', 'Pedro', 'Pablo', 'Maria'], rows),
#     'value': np.random.rand(rows) * 100,
#     'date': pd.to_datetime(np.random.choice(pd.date_range('2021-01-01', '2025-01-01'), rows))
# }
# df = pd.DataFrame(data)
# df.to_csv('datos/test_data.csv', index=False)

# Load dataset
# df = pd.read_csv('datos/test_data.csv')
#
# # Example: Group by name and calculate the mean value
#th result = df.groupby('name')['value'].mean()
# print(result)

path1 = "/tmp"
archivo_csv = f"{path1}/demo.csv"
df2 = pd.read_csv(archivo_csv)
print(f"DF2: {df2}")
print("1>>>",df2.iloc[39])
df3 = df2[df2['edad'] >70 ]

print(f"DF3: {df3}")
df4 = df2[['id','edad','nombre','cedula','salario','estado']]
print(f"DF4: {df4}")
num_nan = df2['edad'].isnull().sum()
print(f"****** df4: \n{df4['nombre']} {df4['cedula']}")
for i in range(5):
  print(f"100>> {i} {df4.iloc[i]['id']} {df4.iloc[i]['nombre']} {df4.iloc[i]['cedula']}")
for i in range(45):
  print(f"{i} {df2.iloc[i]['id']} {df2.iloc[i]['nombre']} {df2.iloc[i]['cedula']}")


print(f"** Número de valores NaN: {num_nan}")
