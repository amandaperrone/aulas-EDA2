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

def reconhece_grafo(mapa):
    
    h, v, info = mapa['h'], mapa['v'], mapa['info']
    
    M = []
    V = {}
    
    # transforma info em uma matriz
    for linha in range(v):
        M.append([]) # M = [] -> [[]] -> [[], []]
        for coluna in range(h):
            M[linha].append(info[linha*h + coluna])
            
    for i in M:
        print(i)

reconhece_grafo(mapa4)

