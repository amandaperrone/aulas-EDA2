class Grafo:

    def __init__(self):
        self.vertices = []
        self.arestas = {}
        self.pesos = {}

    def adicionaVertice(self, valor):
        self.vertices.append(valor)
        self.arestas[valor] = []
    
    def adicionaAresta(self, origem, destino, peso):

        if origem not in self.vertices:
            self.adicionaVertice(origem)

        if destino not in self.vertices:
            self.adicionaVertice(destino)

        self.arestas[origem].append(destino)
        # Caso não seja direcionado, adicionar também a linha abaixo: 
        # self.arestas[destino].append(origem) 
        self.pesos[(origem, destino)] = peso

def menorDistancia(vertices, distancias):

    menor_vertice = None
    menor_distancia = None

    for vertice in vertices:
    
        if menor_vertice is None or distancias[vertice] < menor_distancia:
            menor_vertice = vertice
            menor_distancia = distancias[vertice]
            
    return menor_vertice


# Dijkstra
def dijkstra(grafo, inicio):

    dist = {inicio:0}  # -> {'S': 0}
    T = [inicio]        # Temporário
    P = []              # Permanente

    while len(T) > 0:

        # retorna o vértice de menor distância entre aqueles que estão em T
        v = menorDistancia(T, dist)

        T.pop(T.index(v))
        P.append(v)

        for u in grafo.arestas[v]:
            if u in T:
                # considera a menos distância entre:
                # - a distância que já existia para u
                # - a distância do caminho atual de v -> u
                dist[u] = min(dist[u], dist[v] + grafo.pesos[(v,u)])

            elif u not in P:
                # encontrou um novo nó que não está nem em T nem em P
                dist[u] = dist[v] + grafo.pesos[(v,u)]
                T.append(u)

    return dist



####################

g = Grafo()
# g.adicionaVertice('A')
# g.adicionaVertice('B')

g.adicionaAresta("S", "A", 1)
g.adicionaAresta("S", "B", 5)
g.adicionaAresta("A", "B", 2)
g.adicionaAresta("A", "C", 2)
g.adicionaAresta("A", "D", 1)
g.adicionaAresta("B", "D", 2)
g.adicionaAresta("C", "D", 3)
g.adicionaAresta("C", "E", 1)
g.adicionaAresta("D", "E", 2)

print(g.vertices)
print(g.arestas)
print(g.pesos)

distancias = dijkstra(g, 'S')
print(distancias)
