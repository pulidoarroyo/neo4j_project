from neo4j import GraphDatabase
import csv

# Configuración de la conexión
uri = "bolt://localhost:7687"
user = "neo4j"
password = "12345678"
database = "arbolgenealogico"  # Nombre de la base de datos (puede cambiar según tu configuración)

# Crear una conexión con la base de datos Neo4j
driver = GraphDatabase.driver(uri, auth=(user, password))

# Consulta Cypher para obtener todos los nodos con ciertas propiedades
query = """
    MATCH (n)
    RETURN n.nombre AS nombre, n.edad AS edad, n.actividad AS actividad
"""

# Función para ejecutar la consulta y escribir los resultados en un archivo CSV
def export_to_csv(filename):
    with driver.session(database=database) as session:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # Escribir encabezados
            writer.writerow(["Nombre", "Edad", "Actividad"])
            
            # Ejecutar la consulta y escribir cada registro en el CSV
            result = session.run(query)
            for record in result:
                writer.writerow([record["nombre"], record["edad"], record["actividad"]])

# Nombre del archivo CSV de salida
csv_filename = "exported_data.csv"

# Ejecutar la función para exportar los datos
export_to_csv(csv_filename)

# Cerrar la conexión con la base de datos
driver.close()

print(f"Los datos se han exportado correctamente a '{csv_filename}'.")
