import duckdb
# Load dataset
con = duckdb.connect()
duck_df = con.execute("SELECT * FROM 'datos/test_data.csv'").df()
# Example: Group by name and calculate the mean value
query = "SELECT name, AVG(value) as mean_value FROM duck_df GROUP BY name"
result = con.execute(query).fetchdf()
print(result)