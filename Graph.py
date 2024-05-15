class Graph:
    def __init__(self):
        self.vertices = {}
        self.matrix = []

    def add_vertex(self, name):
        if name not in self.vertices:
            self.vertices[name] = len(self.vertices)
            for row in self.matrix:
                row.append(float('inf'))
            self.matrix.append([float('inf')] * len(self.vertices))
            self.matrix[self.vertices[name]][self.vertices[name]] = 0

    def add_edge(self, src, dest, weight):
        if src in self.vertices and dest in self.vertices:
            src_index = self.vertices[src]
            dest_index = self.vertices[dest]
            self.matrix[src_index][dest_index] = weight

def load_graph(filename, graph):
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            city1, city2, weight = parts[0], parts[1], float(parts[2])
            graph.add_vertex(city1)
            graph.add_vertex(city2)
            graph.add_edge(city1, city2, weight)

def floyd_warshall(graph):
    dist = [row[:] for row in graph.matrix]
    size = len(graph.matrix)
    for k in range(size):
        for i in range(size):
            for j in range(size):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

def find_graph_center(distances):
    eccentricities = [max(row) for row in distances if max(row) < float('inf')]
    min_eccentricity = min(eccentricities)
    return eccentricities.index(min_eccentricity)

def print_shortest_path(distances, graph, src, dest):
    if src in graph.vertices and dest in graph.vertices:
        src_index = graph.vertices[src]
        dest_index = graph.vertices[dest]
        print(f"La ruta más corta de {src} a {dest} tiene un peso de {distances[src_index][dest_index]}")
    else:
        print("Una o ambas ciudades no se encuentran en el grafo.")
def main():
    graph = Graph()
    load_graph(r'D:\Documentos UVG\guategrafo.txt', graph)
    distances = floyd_warshall(graph)

    while True:
        print("\n1. Calcular la ruta más corta entre dos ciudades")
        print("2. Encontrar el centro del grafo")
        print("3. Modificar el grafo")
        print("4. Salir")
        choice = input("Elige una opción: ")

        if choice == '1':
            src = input("Introduce la ciudad origen: ")
            dest = input("Introduce la ciudad destino: ")
            print_shortest_path(distances, graph, src, dest)
        elif choice == '2':
            center = find_graph_center(distances)
            center_city = list(graph.vertices.keys())[center]
            print(f"El centro del grafo está en la ciudad: {center_city}")
        elif choice == '3':
            modify_graph(graph)
            distances = floyd_warshall(graph)  # Recalculamos las distancias después de modificar el grafo
        elif choice == '4':
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

def modify_graph(graph):
    print("Opciones de modificación:")
    print("1. Añadir una nueva conexión")
    print("2. Eliminar una conexión existente")
    print("3. Actualizar el peso de una conexión existente")
    mod_choice = input("Selecciona una opción: ")

    src = input("Introduce la ciudad origen: ")
    dest = input("Introduce la ciudad destino: ")

    if mod_choice == '1':
        weight = float(input("Introduce el nuevo peso: "))
        graph.add_vertex(src)  # Asegura que las ciudades estén en el grafo
        graph.add_vertex(dest)
        graph.add_edge(src, dest, weight)
    elif mod_choice == '2':
        graph.remove_edge(src, dest)
    elif mod_choice == '3':
        new_weight = float(input("Introduce el nuevo peso: "))
        graph.update_edge(src, dest, new_weight)
    else:
        print("Opción no válida. Por favor, elige una opción válida.")



if __name__ == "__main__":
    main()