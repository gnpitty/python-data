import airbyte as ab
import duckdb



#Create the source connection and read the data
source = ab.get_source(
    "source-faker",
    config={"count": 5_000},
    install_if_missing=True
)

source.check()
source.select_all_streams()
result = source.read()

# Load the results from streams to pandas dataframes
products_df = result["products"].to_pandas()
users_df = result["users"].to_pandas()
purchases_df = result["purchases"].to_pandas()

path = '/Users/gerardonunez/Downloads/DATA-seminario'
con = duckdb.connect(f"{path}/my_database.db")
#Write the dataframe data to duckdb tables
con.sql("CREATE TABLE product_dim AS SELECT * FROM products_df")
con.sql("CREATE TABLE user_dim AS SELECT * FROM users_df")
con.sql("CREATE TABLE purchases_fct AS SELECT * FROM purchases_df")

# insert data into the tables from the data frames
con.sql("INSERT INTO product_dim SELECT * FROM products_df")
con.sql("INSERT INTO user_dim SELECT * FROM users_df")
con.sql("INSERT INTO purchases_fct SELECT * FROM purchases_df")

# show data from duck db
con.sql("SELECT * FROM product_dim limit 3").show()
con.sql("SELECT * FROM user_dim limit 3").show()
con.sql("SELECT * FROM purchases_fct limit 3").show()