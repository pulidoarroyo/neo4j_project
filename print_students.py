from neo4j import GraphDatabase

# Configuración de la conexión
uri = "bolt://localhost:7687"
user = "neo4j"
password = "12345678"
database = "arbolgenealogico"  # Nombre de la base de datos (puede cambiar según tu configuración)

# Crear una conexión con la base de datos Neo4j
driver = GraphDatabase.driver(uri, auth=(user, password))

# Consulta Cypher para obtener todas las personas que son estudiantes
query = """
    MATCH (n {actividad: 'Estudiante'})
    RETURN n.nombre AS nombre, n.edad AS edad, n.actividad AS actividad
"""

# Función para ejecutar la consulta y mostrar los resultados en pantalla
def print_students():
    with driver.session(database=database) as session:
        result = session.run(query)
        # Imprimir los resultados en pantalla
        for record in result:
            print(f"Nombre: {record['nombre']}, Edad: {record['edad']}, Actividad: {record['actividad']}")

# Ejecutar la función para imprimir los estudiantes en pantalla
print("Personas que son estudiantes:")
print_students()

# Cerrar la conexión con la base de datos
driver.close()
