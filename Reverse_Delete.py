from collections import deque

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.visitado = []
        self.grafo = [{} for _ in range(self.vertices)]
        
    def adiciona_aresta(self, u, v, peso):
        self.grafo[u][v] = peso
        self.grafo[v][u] = peso
        
    def remove_aresta(self, u, v):
        peso = self.grafo[u][v]
        self.grafo[u].pop(v)
        self.grafo[v].pop(u)
        return [u, v, peso]
        
    def mostra_lista(self):
        for i in range(self.vertices):
            print(f'{i}:', end='  ')
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
        soma = 0
        arestas_removidas = 0
        arestas_minimas = self.vertices - 1
        self.ordena_arestas_maior()

        # Soma total inicial de todas as arestas
        for i in range(self.vertices):
            for j, peso in self.grafo[i].items():
                soma += peso
        soma = soma/2
                
        print(soma)
        for i in range(self.vertices):
            arestas = list(self.grafo[i].items())
            for j, peso in arestas:
                if peso > maiorAresta:
                    maiorAresta = peso  # Use o peso atual diretamente
                    aresta = self.remove_aresta(i, j)
                    print(f'Removendo aresta {aresta}')
                    soma -= peso
                    print(f'Soma após remoção: {soma}')

                    if not self.buscaBFS(0):  # Começa a busca a partir do vértice 0
                        self.adiciona_aresta(aresta[0], aresta[1], aresta[2])
                        soma += peso  # Atualiza a soma após re-adicionar
                        print(f'Soma após re-adicionar: {soma}')
                    else:
                        arestas_removidas += 1  

                    if arestas_removidas >= arestas_minimas:
                        print("Conectividade mínima alcançada. Encerrando o algoritmo.")
                        return soma

        return soma  # Retorna a soma das arestas restantes


    def buscaBFS(self, vertice_inicial):
        self.visitado = ['N' for _ in range(self.vertices)]
        fila = deque([vertice_inicial])
        self.visitado[vertice_inicial] = 'S'

        while fila:
            vertice_atual = fila.popleft()
            for vizinho in self.grafo[vertice_atual]:
                if self.visitado[vizinho] == 'N':
                    fila.append(vizinho)
                    self.visitado[vizinho] = 'S'
        return all(status == 'S' for status in self.visitado)



# Leitura de entrada
while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break

    g = Grafo(m)
    for _ in range(n):
       u, v, peso = map(int, input().split())
       g.adiciona_aresta(u, v, peso)
    g.mostra_lista()
    print("\n\n")
    soma = g.reverse_delete()
    print("\n\n")
    print("Soma final:", soma)
    print("\n\n")
    g.mostra_lista()
