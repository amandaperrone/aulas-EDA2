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

