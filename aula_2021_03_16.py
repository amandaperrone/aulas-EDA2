# retornar o caminho entre A e os vértices

def BFS(G, s):
    visitadosT= [s]

    distLambda = {}
    distLambda[s] = 0

    filaQ = [s]

    caminhos = {}
    caminhos[s] = [s]


    while len(filaQ) > 0:
        u = filaQ.pop(0)

        for v in G[u]:
            if v not in visitadosT:
                filaQ.append(v)
                visitadosT.append(v)
                distLambda[v] = distLambda[u] + 1
                caminhos[v] = caminhos[u].copy() + [v]
                # caminhos[v].append(v)



    return visitadosT, distLambda, caminhos

######################

G = {
  'A' : ['B','C','D'],
  'B' : ['A', 'E'],
  'C' : ['A','G'],
  'D' : ['A','H'],
  'E' : ['B'],
  'F' : [],
  'G' : ['C','H'],
  'H' : ['D','G','I'],
  'I' : ['H']
}

visitados, distancias, caminhos = BFS(G,'A')
print("Visitados:", visitados)
print("Distancias:", distancias)
print("Caminhos:", caminhos)
