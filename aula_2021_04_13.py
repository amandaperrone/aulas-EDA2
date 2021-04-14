# import numpy as np
from numpy import inf

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
        self.arestas[destino].append(origem)
        
        self.pesos[(origem,destino)] = peso
        self.pesos[(destino,origem)] = peso

def floyd(grafo):

    dist = {}

    for i in grafo.vertices:
        for j in grafo.vertices:
            dist[(i,j)] = inf

    for i in grafo.vertices:
        if(i, i) in grafo.pesos and grafo.pesos[(i,i)] < 0:
            dist[(i,i)] = grafo.pesos[(i,i)]
        else:
            dist[(i,i)] = 0

    for i in grafo.vertices:
        for j in grafo.vertices:
            if i != j and (i,j) in grafo.pesos:
                dist[(i,j)] = grafo.pesos[(i,j)]

    for k in grafo.vertices:
        for i in grafo.vertices:
            for j in grafo.vertices:
                dist[(i,j)] = min(dist[(i,j)], dist[(i,k)] + dist[(k,j)])

    
####

g = Grafo()

g.adiciona_aresta("A", "B", 3)
g.adiciona_aresta("A", "D", 10)
g.adiciona_aresta("B", "A", 3)
g.adiciona_aresta("B", "C", 2)
g.adiciona_aresta("C", "B", 2)
g.adiciona_aresta("C", "D", 1)
g.adiciona_aresta("C", "E", 4)
g.adiciona_aresta("D", "A", 10)
g.adiciona_aresta("D", "C", 1)
g.adiciona_aresta("D", "E", 2)
g.adiciona_aresta("E", "C", 4)
g.adiciona_aresta("E", "D", 2)
   

distancias = floyd(g)

##################
#
#      a  b  c  d  e
#    a 0  3  -  10 -
#    b
#    c
#    d
#    e
#
# Começa esparsa e termina densa


# m[0][0]     # matriz com indice numérico
# m['A']['A'] # dicionário de dicionários {'A': {'A': 0}, ...}
# m[(A,A)] = {(A,A): 1, (A,E): 5, ...}