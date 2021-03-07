### mapa do maroto
### estrutura de dados 2

### utilize um mapa inicialmente, depois faça o código rodar em todos eles

""" Mapa 1
>....v
"""
mapa1 = {'h': 6, 'v': 1, 'info': '>....v'}


""" Mapa 2
>.....v
.......
v.....<
...*...
>......
"""
mapa2 = {'h': 7, 'v': 5, 'info': '>.....v.......v.....<...*...>......'}


""" Mapa 3
>.v.
....
*.v.
....
..^.
"""
mapa3 = {'h': 4, 'v': 5, 'info': '>.v.....*.v.......^.'}


""" Mapa 4
>.....v..v
>....*....
^.....<..^
"""
mapa4 = {'h': 10, 'v': 3, 'info': '>.....v..v>....*....^.....<..^'}

nColunas = mapa4["h"]
nLinhas = mapa4["v"]



# DICAS:
#
# (1) pense como ler os dados do mapa e transformar em um grafo, (os mapas são dicionários) 
#     cada direção é um vértice e aponta com qual vértice seguinte se conecta
#
# (2) as arestas não devem ser utilizadas duas vezes para eles não se perderem no castelo
#
# (3) utilize papel e caneta para verificar se as informações de vértices e arestas estão corretas
#     a medida que você implementar
#
# (4) ao final, basta imprimir qual é o mapa CORRETO, para todos os outros apenas ignore


# --------------- TENTATIVA 1 USANDO MAPA 4

### CONSTRUIR MATRIZ

nColunas = mapa4["h"]
nLinhas = mapa4["v"]
nConteudo = mapa4["info"]

def construirMapa (colunas, linhas, conteudo):
    mapaPronto = []
    cont = 0
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(conteudo[cont])
            cont = cont +1 
        mapaPronto.append(linha)
    return mapaPronto

# Imprimir matriz
mapaPronto = construirMapa(nColunas, nLinhas, list(nConteudo))
#print(mapaPronto)

### ANALISAR AS ADJACÊNCIAS

def teste (mapa):
    x = 0
    y = 0
    listaVertices = []
    for teste1 in range(nColunas):
        if mapa[x][y] != '.':
            listaVertices.append((mapa[x][y], x, y))
            print(mapa[x][y])
        y = y + 1
    return listaVertices

lista = teste(mapaPronto)
print(lista)
arestas = []

vertices = []
n1 = 1
for x in lista:
    n2 = 'V' + str(n1) 
    print(n2)
    n1 = n1 + 1
    vertices.append(n2)
print(vertices)

if len(lista) > 1:
    arestas.append(())
    print("Tem mais um vertice na linha")

# E3 = [('Q1', 'Q2'), ('Q1', 'Q3'), ('Q2','Q1'),('Q3', 'Q1')]
