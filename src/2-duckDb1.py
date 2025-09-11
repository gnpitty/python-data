import duckdb

    # Connect to or create a persistent database file named 'my_database.db'
path = '../data'
#con = duckdb.connect(f"{path}/my_database.db")
con = duckdb.connect()
con.execute( f"CREATE TABLE demo30k AS SELECT * from '{path}/demo30K.csv'")
result = con.execute("SELECT * FROM demo30k").fetchdf()
print(result)
