# retorna também o caminho entre A e os vértices da função BFS

def BFS(G,s):    
    visitadosT = [s]    
    
    caminhos = {}    
    caminhos[s] = [s]    
    
    distLambda = {}    
    distLambda[s] = 0    
    
    filaQ = [s]    
    
    while len(filaQ) > 0:        
        u = filaQ.pop(0)   # -> u: 'A'        
        
        for v in G[u]:   # u----v            
            if v not in visitadosT:                
                filaQ.append(v)                
                visitadosT.append(v)
                
                distLambda[v] = distLambda[u] + 1                
                caminhos[v] = caminhos[u].copy()                
                caminhos[v].append(v)    

    return visitadosT, distLambda, caminhos
        
####################################

G = {  
    'S' : ['A'],
    'A' : ['B','C','D'],  
    'B' : [],  
    'C' : [],  
    'D' : ['G','H'],  
    'E' : ['G'],  
    'F' : [],  
    'G' : [],  
    'H' : [],  
}

visitados, distancias, caminhos = BFS(G,'A')

print("Visitados:", visitados)
# print("Distâncias:", distancias)
# print("Caminhos:", caminhos)

disponiveis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

naoPercorrido = list(set(disponiveis) - set(visitados))
print("Os vertices nao percorridos sao: ",naoPercorrido)