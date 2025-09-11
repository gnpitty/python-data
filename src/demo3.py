import json
import pandas as pd

from ydata_profiling import ProfileReport
from ydata_profiling.utils.cache import cache_file

file_name = cache_file(
    "titanic.csv",
    "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv",
)
df = pd.read_csv(file_name)
print(df.head())
print(df.describe())

type_schema = {"Survived": "categorical", "Embarked": "categorical"}

# We can set the type_schema only for the variables that we are certain of their types.
# All the other will be automatically inferred.
report = ProfileReport(df, title="Titanic EDA", type_schema=type_schema)

report.to_file("salida/titanic-report.html")