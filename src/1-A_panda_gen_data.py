import pandas as pd
import numpy as np
import datetime
# Generate dataset
rows = 10_000_000
np.random.seed(42)
data = {
    'id': np.arange(rows),
    'name': np.random.choice(['Juan', 'Pedro', 'Pablo', 'Maria'], rows),
    'value': np.random.rand(rows) * 100,
    'date': pd.to_datetime(np.random.choice(pd.date_range('2021-01-01', '2025-01-01'), rows))
}
df = pd.DataFrame(data)
df.to_csv('datos/test_data.csv', index=False)

