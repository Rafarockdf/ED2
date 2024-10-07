class no:
    def __init__(self,chave):
        self.chave=chave
        self.proximo = None
        self.anterior = None
        
class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        
    def inserir(self,valor):
        novo = no(valor)
        if self.inicio == None:
            self.inicio = novo
            novo.anterior = self.inicio
        else:
            novo.proximo = self.inicio  
            self.inicio.anterior = novo  
            self.inicio = novo
            
            
class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.visitado = []
        self.grafo = [[] for _ in range(self.vertices)]
        
    def adiciona_aresta(self, u, v):
        self.grafo[u-1].append(v)
        self.grafo[v-1].append(u)
        
    def mostra_lista(self):
        for i in range(self.vertices):
            print(f'{i+1}:', end='  ')
            for j in self.grafo[i]:
                print(f' -> {j}', end='  ')
            print('')
         
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
            
            
g = Grafo(12)
# 1
g.adiciona_aresta(1,2)
g.adiciona_aresta(1,4)
g.adiciona_aresta(1,5)
# 2
g.adiciona_aresta(2,5)
g.adiciona_aresta(2,7)
g.adiciona_aresta(2,3)
g.adiciona_aresta(2,9)
# 3
g.adiciona_aresta(3,12)
g.adiciona_aresta(3,6)
g.adiciona_aresta(3,10)
# 4
g.adiciona_aresta(4,5)
g.adiciona_aresta(4,7)
# 5
g.adiciona_aresta(5,8)
g.adiciona_aresta(5,6)
# 6
g.adiciona_aresta(6,9)
g.adiciona_aresta(6,11)
# 7
g.adiciona_aresta(7,8)
# 8
g.adiciona_aresta(8,9)
# 9
g.adiciona_aresta(9,12)
g.adiciona_aresta(9,10)
# 10
g.adiciona_aresta(10,11)
# 11
g.adiciona_aresta(11,12)



g.buscaDFS()