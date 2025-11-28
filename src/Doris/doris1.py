import pymysql
import pymysql.cursors
import time

def consultar_clientes_doris():
    # 1. Configuración de la conexión
    # El puerto por defecto para consultas (Query Port) en Doris FE es 9030
    config = {
        'host': 'alma-gncon2',  # Tu IP del nodo FE de Doris
        'port': 9030,  # Puerto MySQL de Doris (No confundir con 8030/8040)
        'user': 'admin',  # Usuario (por defecto suele ser admin)
        'password': '',  # Tu contraseña
        'database': 'demo',  # Nombre de tu DB
        'cursorclass': pymysql.cursors.DictCursor  # Para recibir datos como diccionario
    }

    connection = None

    try:
        print("🔌 Conectando a Apache Doris...")
        connection = pymysql.connect(**config)

        with connection.cursor() as cursor:
            # 2. Definir la consulta
            # Limitamos a 10 para no saturar la memoria si la tabla es gigante
            sql = """SELECT * FROM cliente WHERE salario > 80000 
                and (direccion like '%Avenida%' 
                OR descripcion like '%horas%'
                OR profesion like '%Agente%') LIMIT 100 """

            # 3. Ejecutar la consulta
            start_time = time.perf_counter()

            print(f"🔄 Ejecutando: {sql}")
            cursor.execute(sql)

            # 4. Obtener resultados
            result = cursor.fetchall()
            end_time = time.perf_counter()
            print(f"✅ Se encontraron {end_time-start_time} numero {len(result)} registros:\n")

            for row in result:
                print(row)

    except pymysql.MySQLError as e:
        print(f"❌ Error al conectar o consultar Doris: {e}")

    finally:
        # 5. Cerrar la conexión
        if connection:
            connection.close()
            print("\n🔒 Conexión cerrada.")


if __name__ == "__main__":
    consultar_clientes_doris()