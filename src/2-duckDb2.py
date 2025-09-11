import duckdb

path = '/Users/gerardonunez/Downloads/DATA-seminario'

def desplegar_query(label,con,query):
    res = con.execute(query)
    for row in res.fetchall():
      print(f"{label}--> {row}")

with duckdb.connect(f"{path}/my_database.db")as con:
    desplegar_query("Conteo:",con, "Select count(*) from demo8")
    desplegar_query("Cedulas Provs:",con, "Select count(*), split_part(cedula, '-', 1) as prov from demo8 group by split_part(cedula, '-', 1) order by prov  desc")
    desplegar_query("Rows: ",con,   "SELECT nombre,cedula,edad,fecha_nacimiento  FROM demo8 Limit 5")
    desplegar_query("Rows2:",con,  "Select * from demo8 Where edad is NULL limit 10")
