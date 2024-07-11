from neo4j import GraphDatabase

# Configuración de la conexión
uri = "bolt://localhost:7687"
user = "neo4j"
password = "12345678"
database = "arbolgenealogico"  # Nombre de la base de datos (puede cambiar según tu configuración)

# Consulta Cypher para obtener los primos del amigo de Magleo
query = """
    MATCH (hijo:Hombre {nombre: 'Magleo'})-[:AMIGO_DE]->(amigo)-[:PRIMO_DE]->(primo)
    RETURN amigo.nombre AS Nombre_del_amigo, primo.nombre AS Nombre_del_primo, primo.edad AS Edad_del_primo, primo.actividad AS Actividad_del_primo
"""

# Función para ejecutar la consulta y mostrar los resultados en pantalla
def print_primos_del_amigo_de_magleo():
    with GraphDatabase.driver(uri, auth=(user, password)) as driver:
        with driver.session(database=database) as session:
            result = session.run(query)
            # Imprimir los resultados en pantalla
            for record in result:
                print(f"Nombre del amigo: {record['Nombre_del_amigo']}")
                print(f"Nombre del primo: {record['Nombre_del_primo']}, Edad: {record['Edad_del_primo']}, Actividad: {record['Actividad_del_primo']}")
                print("---")

    # Cerrar la conexión con la base de datos
    driver.close()

# Ejecutar la función para imprimir los primos del amigo de Magleo en pantalla
print("Primos del amigo de Magleo:")
print_primos_del_amigo_de_magleo()
