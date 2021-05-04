# Estrutura de Dados e Algoritmos II
# AC2 - Árvores geradoras e mínimas

# Amanda Perrona Degrande 140501
# Juliana Cristina Ferreira Izac 190778
# Leonardo Coelho Ruas 190089
# Lissa Bruna Urbano 120780
# Octávio Henrique Müller Barrio 190067
# Raquel Kuntz Oliveira 121036

# Arvore Geradora

from collections import defaultdict
from pprint import pprint


class Grafo:

    def __init__(self):
        self.vertices = []
        self.arestas = defaultdict(list)

    def adiciona_vertice(self, valor):

        self.vertices.append(valor)
        self.arestas[valor] = []

    def adiciona_aresta(self, origem, destino):

        if origem not in self.vertices:
            self.adiciona_vertice(origem)

        if destino not in self.vertices:
            self.adiciona_vertice(destino)

        self.arestas[origem].append(destino)
        self.arestas[destino].append(origem)


# algoritmo BFS modificado
def obterArvoreGeradora(G, s):

    visitadosT = [s]

    caminhos = {}
    caminhos[s] = [s]

    filaQ = [s]

    arestas = [s]

    while len(filaQ) > 0:
        u = filaQ.pop(0)

        for v in G[u]:
            if v not in visitadosT:
                arestas.append(v)  # guardando as arestas inéditas
                filaQ.append(v)
                visitadosT.append(v)

                caminhos[v] = caminhos[u].copy()
                caminhos[v].append(v)

    return visitadosT, caminhos, arestas


def adicionarArestasEspeciais(mapa, usaAereo, usaAquatico):

    # caminhos aereos
    if usaAereo:
        mapa.adiciona_aresta("Dewford", "Littleroot")
        mapa.adiciona_aresta("Dewford", "Pacifidlog")
        mapa.adiciona_aresta("Fortree", "Pacifidlog")
        mapa.adiciona_aresta("Lavaridge", "Mauville")
        mapa.adiciona_aresta("Lilycove", "Mauville")
        mapa.adiciona_aresta("Mauville", "Pacifidlog")
        mapa.adiciona_aresta("Mossdeep", "Pacifidlog")
        mapa.adiciona_aresta("Petalburg", "Verdanturf")

    # caminhos aquaticos
    if usaAquatico:
        mapa.adiciona_aresta("Dewford", "Petalburg")
        mapa.adiciona_aresta("Dewford", "Slateport")
        mapa.adiciona_aresta("Ever Grand", "Lilycove")
        mapa.adiciona_aresta("Ever Grand", "Pacifidlog")
        mapa.adiciona_aresta("Ever Grand", "Sootopolis")
        mapa.adiciona_aresta("Lilycove", "Mossdeep")
        mapa.adiciona_aresta("Lilycove", "Sootopolis")
        mapa.adiciona_aresta("Mossdeep", "Sootopolis")
        mapa.adiciona_aresta("Pacifidlog", "Slateport")
        mapa.adiciona_aresta("Pacifidlog", "Sootopolis")


###############
g = Grafo()

# caminhos terrestres
g.adiciona_aresta("Fallarbor", "Mauville")
g.adiciona_aresta("Fallarbor", "Rustboro")
g.adiciona_aresta("Fortree", "Lilycove")
g.adiciona_aresta("Fortree", "Mauville")
g.adiciona_aresta("Mauville", "Verdanturf")
g.adiciona_aresta("Mauville", "Slateport")
g.adiciona_aresta("Oldale", "Petalburg")
g.adiciona_aresta("Petalburg", "Rustboro")
g.adiciona_aresta("Rustboro", "Verdanturf")
g.adiciona_aresta("Littleroot", "Oldale")

# habilitar/desabilitar o trafego nas rotas aereas e aquaticas
adicionarArestasEspeciais(mapa=g, usaAereo=False, usaAquatico=False)

# chamada do algoritmo BFS modificado, obterArvoreGeradora
visitados, caminhos, arestas = obterArvoreGeradora(g.arestas, "Rustboro")
print("Visitados:", visitados)
print("Caminhos:")
pprint(caminhos)
print("Arestas:")
pprint(arestas)
