from collections import deque
class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.visitado = []
        self.grafo = [{} for _ in range(self.vertices)]
        
    def adiciona_aresta(self, u, v,peso):
        self.grafo[u - 1][v] = peso
        self.grafo[v - 1][u] = peso
        
    def remove_aresta(self, u, v, peso):
        pass
        
    def mostra_lista(self):
        for i in range(self.vertices):
            print(f'{i+1}:', end='  ')
            for j in self.grafo[i]:
                print(f'-> {j} peso {self.grafo[i][j]}', end=' ')
            print('')
            
    def ordena_arestas_maior(self):
        for i in range(self.vertices):
            # Ordena o dicionário `self.grafo[i]` pelos valores dos pesos
            elementos_ordenados = sorted(self.grafo[i].items(), key=lambda item: item[1], reverse=True)  # item[1] refere-se ao peso
            # Converte a lista ordenada de tuplas de volta para um dicionário
            self.grafo[i] = dict(elementos_ordenados)
            
    def reverse_delete(self):
        maiorAresta = 0
        for i in range(self.vertices):
            for j in self.grafo[i]:
                if self.grafo[i][j] > maiorAresta:
                    maiorAresta  = self.grafo[i][j]
                    
                
    def buscaDFS(self):
        self.visitado = ['N' for _ in range(self.vertices)]
        
        for i in range(self.vertices):  # Itera sobre os vértices
            if self.visitado[i] == 'N':
                print(f'Iniciando DFS a partir do vértice {i+1}')
                self.buscaDFSProf(i)
                
    def buscaDFSProf(self, posicao):
        self.visitado[posicao] = 'S'
        print(f'Visitando vértice {posicao+1}')
        
        for i in self.grafo[posicao]:
            if self.visitado[i-1] == 'N':  # Corrige índice (i-1) para acessar corretamente
                self.buscaDFSProf(i-1)
# Exemplo de uso
    def buscaBFS(self, vertice_inicial):
        # Iniciando a lista de vértices visitados
        self.visitado = ['N' for _ in range(self.vertices)]
        
        # Inicializando a fila (queue) e marcando o vértice inicial como visitado
        fila = deque([vertice_inicial])
        self.visitado[vertice_inicial - 1] = 'S'
        print(f'Iniciando BFS a partir do vértice {vertice_inicial}')
        
        while fila:
            # Remove o vértice da fila (usamos o termo "desenfileirar")
            vertice_atual = fila.popleft()
            print(f'Visitando vértice {vertice_atual}')
            
            # Explorar os vértices adjacentes
            for vizinho in self.grafo[vertice_atual - 1]:
                if self.visitado[vizinho - 1] == 'N':
                    fila.append(vizinho)
                    self.visitado[vizinho - 1] = 'S'
                    print(f'Colocando vértice {vizinho} na fila')  


g = Grafo(6)
# 1
g.adiciona_aresta(1,2,5)
g.adiciona_aresta(1,3,6)
g.adiciona_aresta(1,4,4)
#2
g.adiciona_aresta(2,3,1)
g.adiciona_aresta(2,4,2)
#3
g.adiciona_aresta(3,4,2)
g.adiciona_aresta(3,5,5)
g.adiciona_aresta(3,6,3)
#4
g.adiciona_aresta(4,6,4)
#5
g.adiciona_aresta(5,6,4)

g.ordena_arestas_maior()
g.mostra_lista()        

g.reverse_delete()
