# MATRIZ DE ADJACÊNCIA
# q1---q3
# |
# q2
print("MATRIZ DE ADJACENCIA")
V1 = ['Q1', 'Q2', 'Q3']
E2 = [('Q1', 'Q2'), ('Q1', 'Q3'), ('Q2','Q1'),('Q3', 'Q1')]

M = []
for _ in V1: #undescore não pega valor, pois não iremos utilizar
    # M.append([]) # output [[], [], []]
    M.append([0] * len(V1)) # output [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for origem, destino in E2:
    M[V1.index(origem)][V1.index(destino)] = 1

print(M)
print("\n")


# LISTA DE ADJACÊNCIA
# q1---q3
# |
# q2
print("LISTA DE ADJACENCIA")
V2 = ['Q1', 'Q2', 'Q3']
E2 = [('Q1', 'Q2'), ('Q1', 'Q3'), ('Q2','Q1'),('Q3', 'Q1')]

L = []

for _ in V2: #undescore não pega valor, pois não iremos utilizar
    L.append([])

for origem, destino in E2:
    # L[V2.index(origem)].append(V2.index(destino)) # mostra índices
    L[V2.index(origem)].append(destino) # mostra o detalhe

print(L)
print("\n")


# DICIONÁRIOS
# São armazenados em hash, com par de chave-valor
# q1---q3
# |
# q2

print("DICIONARIO")

V3 = ['Q1', 'Q2', 'Q3']
E3 = [('Q1', 'Q2'), ('Q1', 'Q3'), ('Q2','Q1'),('Q3', 'Q1')]

# dicio = {'Q1': ['Q2', 'Q4'], 'Q2': ['Q1'], 'Q3': ['Q1']}

# Inicializar um dicionário
# A = { }

L = {}
for v in V3:
    L[v] = []

for origem, destino in E3:
    L[origem].append(destino)

print(L)
print("\n")

