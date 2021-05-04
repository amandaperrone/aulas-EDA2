class Grafo:
    
    def __init__(self):
        self.vertices = []
        self.arestas = {}
        self.pesos = {}
        
    def adiciona_vertice(self, valor):
        self.vertices.append(valor)
        self.arestas[valor] = []
        
    def adiciona_aresta(self, origem, destino, peso):
        
        if origem not in self.vertices:
            self.adiciona_vertice(origem)
            
        if destino not in self.vertices:
            self.adiciona_vertice(destino)
        
        self.arestas[origem].append(destino)
        self.pesos[(origem,destino)] = peso
        
        
def menor_distancia(vertices, distancias):
    
    menor_vertice   = None
    menor_distancia = None
    
    for vertice in vertices:
    
        if menor_vertice is None or distancias[vertice] < menor_distancia:
            menor_vertice = vertice
            menor_distancia = distancias[vertice]
            
    return menor_vertice


def dijkstra(grafo, inicio):
    
    dist = {inicio:0} # -> {'S':0}
    
    T = [inicio] # -> temporario
    P = []       # -> permanente
    
    while len(T) > 0:
        
        # retorna o vertice de menor distancia entre aqueles que estão em T
        v = menor_distancia(T, dist)
        
        T.pop(T.index(v))
        P.append(v)
        
        for u in grafo.arestas[v]:
            
            if u in T:
                
                # considera a menor distancia entre:
                # - a distancia que ja existia pra u
                # - a distancia do caminho atual de v -> u
                dist[u] = min(dist[u], dist[v] + grafo.pesos[(v,u)])

            elif u not in P:

                # encontrou um novo no que nao esta nem em T nem em P
                dist[u] = dist[v] + grafo.pesos[(v,u)]
                T.append(u)

    return dist

###############

g = Grafo()

g.adiciona_aresta("S", "A", 8)
g.adiciona_aresta("A", "B", 4)
g.adiciona_aresta("A", "C", 5)
g.adiciona_aresta("A", "D", 8)
g.adiciona_aresta("D", "E", 8)
g.adiciona_aresta("D", "G", 4)
g.adiciona_aresta("D", "H", 4)
g.adiciona_aresta("E", "G", 1)
g.adiciona_aresta("E", "F", 6)


# print(g.vertices)
# print(g.arestas)
# print(g.pesos)

distancias = dijkstra(g, 'S')

print(distancias)

pressaoInicial = 0

for v in g.vertices:
    if (distancias[v] > pressaoInicial):
        pressaoInicial = distancias[v]

print(pressaoInicial, "eh a pressao inicial minima.")

