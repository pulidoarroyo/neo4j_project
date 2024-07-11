from neo4j import GraphDatabase

# Configuración de la conexión
uri = "bolt://localhost:7687"
user = "neo4j"
password = "12345678"
database = "arbolgenealogico"  # Nombre de la base de datos (puede cambiar según tu configuración)

# Consulta Cypher para obtener los primos de Magleo
query = """
    MATCH (hijo:Hombre {nombre: 'Magleo'})-[:PRIMO_DE]->(primo)
    RETURN primo.nombre AS Nombre, primo.edad AS Edad, primo.actividad AS Actividad
"""

# Función para ejecutar la consulta y mostrar los resultados en pantalla
def print_primos_de_magleo():
    with GraphDatabase.driver(uri, auth=(user, password)) as driver:
        with driver.session(database=database) as session:
            result = session.run(query)
            # Imprimir los resultados en pantalla
            for record in result:
                print(f"Nombre: {record['Nombre']}, Edad: {record['Edad']}, Actividad: {record['Actividad']}")

    # Cerrar la conexión con la base de datos
    driver.close()

# Ejecutar la función para imprimir los primos de Magleo en pantalla
print("Primos de Magleo:")
print_primos_de_magleo()

