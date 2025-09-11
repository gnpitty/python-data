import pandas as pd
from ydata_profiling import ProfileReport

# creating the dataframe
# dictionary of data
dct = {'ID': {0: 23, 1: 43, 2: 12, 3: 13,
              4: 67, 5: 89, 6: 90, 7: 56,
              8: 34},
       'Name': {0: 'Ram', 1: 'Deep', 2: 'Yash',
                3: 'Aman', 4: 'Arjun', 5: 'Aditya',
                6: 'Divya', 7: 'Chalsea',
                8: 'Akash' },
       'Marks': {0: 89, 1: 97, 2: 45, 3: 78,
                 4: 56, 5: 76, 6: 100, 7: 87,
                 8: 81},
       'Grade': {0: 'B', 1: 'A', 2: 'F', 3: 'C',
                 4: 'E', 5: 'C', 6: 'A', 7: 'B',
                 8: 'B'}
      }

# forming dataframe and printing
data = pd.DataFrame(dct)
print(data)

# Create a profile report
profile = ProfileReport(data, title="Demo  ydata_profiling ")

# Display the profile report in a Jupyter notebook or JupyterLab
# profile.to_widgets()

# Save the profile report to an HTML file
profile.to_file("salida/ydata_profiling_report.html")