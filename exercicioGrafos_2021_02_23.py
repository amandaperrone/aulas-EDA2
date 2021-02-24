# Representar o grafo abaixo por matriz de adjacência e linha de adjacência
# https://runestone.academy/runestone/books/published/pythonds/_images/wordgraph.png

V = ['sage','sale','page','pale','pole','pope','poll','pool','cool','fool','foul','foil','fail','fall','pall']
#print(len(V))
E = [('sage', 'sale'), ('sage', 'page'), ('sale', 'pale'), ('sale', 'sage'), ('page', 'sage'), ('page', 'pale'), ('pale', 'sale'), ('pale', 'page'), ('pale', 'pall'), ('pale', 'pole'), ('pole', 'pope'), ('pole', 'pale'), ('pole', 'poll'), ('pope', 'pole'), ('poll', 'pole'), ('poll', 'pall'), ('poll', 'pool'), ('pool', 'poll'), ('pool', 'cool'), ('pool', 'fool'), ('cool', 'pool'), ('cool', 'fool'), ('fool', 'pool'), ('fool', 'cool'), ('fool', 'foul'), ('fool', 'foul'), ('foul', 'fool'), ('foul', 'foil'), ('foil', 'fool'), ('foil', 'foul'), ('foil', 'fail'), ('fail', 'foil'), ('fail', 'fall'), ('fall', 'fail'), ('fall', 'pall'), ('pall', 'fall'), ('pall', 'pool'), ('pall', 'pale')]

MATRIZ = []

for _ in V:
    MATRIZ.append([0] * len(V))

#print(MATRIZ) # gera-se uma matriz 15X15

for origem, destino in E:
    MATRIZ[V.index(origem)][V.index(destino)] = 1

print(MATRIZ)



LISTA = []

for _ in V:
    LISTA.append([])

for origem, destino in E:
    LISTA[V.index(origem)].append(destino)

print(LISTA)