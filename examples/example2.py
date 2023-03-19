from JGVutils import Utils, MySQLConnection

# Capturar la conexión
conexion = MySQLConnection(host="localhost", dbname="wordle")

# Comprobar si existe conexión
if conexion.is_database_connection():
    # Realizar una query sencilla
    filas = conexion.execute_query("SELECT * FROM palabras", [], "as")
    # Imprimir los datos
    print(Utils.return_json(filas))
else:
    print("No existe conexión")

