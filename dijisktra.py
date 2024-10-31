import heapq

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for _ in range(self.vertices)]
        self.map_letras_para_indices = {}
        self.map_indices_para_letras = {}

    def adiciona_vertice(self, letra, indice):
        self.map_letras_para_indices[letra] = indice
        self.map_indices_para_letras[indice] = letra

    def adiciona_aresta(self, u, v, peso):
        u_idx = self.map_letras_para_indices[u]
        v_idx = self.map_letras_para_indices[v]
        self.grafo[u_idx - 1].append((v_idx, peso))
        self.grafo[v_idx - 1].append((u_idx, peso))

    def mostra_lista(self):
        for i in range(self.vertices):
            letra = self.map_indices_para_letras[i + 1]
            print(f'{letra}:', end='  ')
            for v, peso in self.grafo[i]:
                v_letra = self.map_indices_para_letras[v]
                print(f' -> {v_letra}(peso: {peso})', end='  ')
            print('')

    def dijkstra(self, inicio):
        inicio_idx = self.map_letras_para_indices[inicio]
        distancias = {i: float('inf') for i in range(1, self.vertices + 1)}
        predecessores = {i: None for i in range(1, self.vertices + 1)}
        distancias[inicio_idx] = 0
        visitado = set()
        fila_prioridade = [(0, inicio_idx)]
        
        while fila_prioridade:
            dist_atual, vertice_atual = heapq.heappop(fila_prioridade)
            
            if vertice_atual in visitado:
                continue
            
            visitado.add(vertice_atual)
            
            for vizinho, peso in self.grafo[vertice_atual - 1]:
                distancia = dist_atual + peso
                
                if distancia < distancias[vizinho]:
                    distancias[vizinho] = distancia
                    predecessores[vizinho] = vertice_atual
                    heapq.heappush(fila_prioridade, (distancia, vizinho))
        
        return distancias, predecessores

    def caminho_para(self, predecessores, inicio, destino):
        caminho = []
        destino_idx = self.map_letras_para_indices[destino]
        atual = destino_idx
        while atual:
            caminho.append(self.map_indices_para_letras[atual])
            atual = predecessores[atual]
        caminho.reverse()
        return caminho

# Criando o grafo com 12 vértices
g = Grafo(12)

# Adicionando os vértices e mapeando-os com letras
g.adiciona_vertice('a', 1)
g.adiciona_vertice('b', 2)
g.adiciona_vertice('c', 3)
g.adiciona_vertice('d', 4)
g.adiciona_vertice('e', 5)
g.adiciona_vertice('f', 6)
g.adiciona_vertice('g', 7)
g.adiciona_vertice('h', 8)
g.adiciona_vertice('i', 9)
g.adiciona_vertice('j', 10)
g.adiciona_vertice('l', 11)
g.adiciona_vertice('m', 12)

# Adicionando as arestas
g.adiciona_aresta('a', 'b', 42)
g.adiciona_aresta('a', 'd', 61)
g.adiciona_aresta('a', 'c', 50)
g.adiciona_aresta('b', 'd', 29)
g.adiciona_aresta('b', 'j', 17)
g.adiciona_aresta('c', 'd', 42)
g.adiciona_aresta('c', 'e', 67)
g.adiciona_aresta('d', 'e', 45)
g.adiciona_aresta('d', 'f', 29)
g.adiciona_aresta('d', 'j', 17)
g.adiciona_aresta('e', 'f', 72)
g.adiciona_aresta('e', 'g', 64)
g.adiciona_aresta('e', 'i', 62)
g.adiciona_aresta('f', 'j', 30)
g.adiciona_aresta('f', 'g', 25)
g.adiciona_aresta('f', 'l', 52)
g.adiciona_aresta('g', 'h', 35)
g.adiciona_aresta('g', 'l', 47)
g.adiciona_aresta('h', 'i', 31)
g.adiciona_aresta('h', 'm', 32)
g.adiciona_aresta('i', 'm', 25)
g.adiciona_aresta('l', 'm', 30)

# Executando o algoritmo de Dijkstra partindo do vértice 'G'
distancias, predecessores = g.dijkstra('G')

# Mostrando a tabela de distâncias
print("Tabela de distâncias de 'G' até as áreas dos pacientes:")
for paciente in ['O', 'E', 'D', 'X', 'T']:
    print(f"Distância até {paciente}: {distancias[g.map_letras_para_indices[paciente]]}")

# Mostrando o caminho para o paciente T
caminho_para_T = g.caminho_para(predecessores, 'G', 'T')
print(f"Caminho de G até T: {' -> '.join(caminho_para_T)}")


g2 = Grafo(11)
g2.adiciona_vertice('O', 1)
g2.adiciona_vertice('R', 2)
g2.adiciona_vertice('K', 3)
g2.adiciona_vertice('G', 4)
g2.adiciona_vertice('E', 5)
g2.adiciona_vertice('A', 6)
g2.adiciona_vertice('Q', 7)
g2.adiciona_vertice('M', 8)
g2.adiciona_vertice('D', 9)
g2.adiciona_vertice('T', 10)
g2.adiciona_vertice('X', 11)

g2.adiciona_aresta('O', 'R', 4)
g2.adiciona_aresta('O', 'G', 2)
g2.adiciona_aresta('O', 'K', 1)
g2.adiciona_aresta('R', 'G', 1)
g2.adiciona_aresta('R', 'E', 0)
g2.adiciona_aresta('K', 'G', 1)
g2.adiciona_aresta('G', 'E', 3)
g2.adiciona_aresta('G', 'A', 1)
g2.adiciona_aresta('G', 'Q', 5)
g2.adiciona_aresta('E', 'A', 2)
g2.adiciona_aresta('A', 'Q', 2)
g2.adiciona_aresta('A', 'D', 1)
g2.adiciona_aresta('A', 'T', 4)
g2.adiciona_aresta('D', 'T', 3)
g2.adiciona_aresta('D', 'X', 3)
g2.adiciona_aresta('T', 'X', 4)
g2.adiciona_aresta('M', 'Q', 2)

# Executando o algoritmo de Dijkstra partindo do vértice 'G'
distancias, predecessores = g2.dijkstra('G')

# Mostrando a tabela de distâncias
print("Tabela de distâncias de 'G' até as áreas dos pacientes:")
for paciente in ['O', 'E', 'D', 'X', 'T']:
    print(f"Distância até {paciente}: {distancias[g2.map_letras_para_indices[paciente]]}")

# Mostrando o caminho para o paciente T
caminho_para_T = g2.caminho_para(predecessores, 'G', 'T')
print(f"Caminho de G até T: {' -> '.join(caminho_para_T)}")