from neo4j import GraphDatabase

# Configuración de la conexión
uri = "bolt://localhost:7687"
user = "neo4j"
password = "12345678"
database = "arbolgenealogico"  # Nombre de la base de datos (puede cambiar según tu configuración)

# Crear una conexión con la base de datos Neo4j
driver = GraphDatabase.driver(uri, auth=(user, password))

# Consulta Cypher para obtener todos los nodos
query = """
    MATCH (n)
    RETURN n
"""

# Función para ejecutar la consulta y mostrar los nodos de forma ordenada
def check_nodes():
    with driver.session(database=database) as session:
        result = session.run(query)
        # Imprimir los nodos
        for record in result:
            node = record["n"]
            labels = list(node.labels)
            properties = dict(node._properties)
            # Formatear la salida
            print(f"Nodo ID: {node.id}, Labels: {labels}, Propiedades: {properties}")

# Ejecutar la función para imprimir los nodos de forma ordenada
print("Nodos en la base de datos Neo4j:")
check_nodes()

# Cerrar la conexión con la base de datos
driver.close()
