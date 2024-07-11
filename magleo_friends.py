from neo4j import GraphDatabase

# Configuración de la conexión
uri = "bolt://localhost:7687"
user = "neo4j"
password = "12345678"
database = "arbolgenealogico"  # Nombre de la base de datos (puede cambiar según tu configuración)

# Consulta Cypher para obtener los amigos de Magleo
query = """
    MATCH (m:Hombre {nombre: 'Magleo'})-[:AMIGO_DE]-(amigo)
    RETURN amigo.nombre AS Nombre_del_amigo, amigo.edad AS Edad_del_amigo, amigo.actividad AS Actividad_del_amigo
"""

# Función para ejecutar la consulta y mostrar los resultados en pantalla
def print_friends_of_magleo():
    with GraphDatabase.driver(uri, auth=(user, password)) as driver:
        with driver.session(database=database) as session:
            result = session.run(query)
            # Imprimir los resultados en pantalla
            for record in result:
                print(f"Nombre: {record['Nombre_del_amigo']}, Edad: {record['Edad_del_amigo']}, Actividad: {record['Actividad_del_amigo']}")


    # Cerrar la conexión con la base de datos
    driver.close()

# Ejecutar la función para imprimir los amigos de Magleo en pantalla
print("Amigos de Magleo:")
print_friends_of_magleo()
