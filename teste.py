from collections import deque, defaultdict

def encontrar_caminho(grafo, emparelhamento, pai, raiz):
    # BFS para encontrar o caminho de aumento
    visitados = {raiz}
    fila = deque([raiz])
    base = {}
    
    for vertice in grafo:
        base[vertice] = vertice

    while fila:
        u = fila.popleft()
        for v in grafo[u]:
            # Se v já está no mesmo flor (blossom)
            if base[u] == base[v]:
                continue

            # Encontrou um caminho de aumento
            if v not in visitados:
                visitados.add(v)
                pai[v] = u

                if v not in emparelhamento:
                    return v
                else:
                    x = emparelhamento[v]
                    visitados.add(x)
                    fila.append(x)
                    pai[x] = v
            # Encontrou um ciclo ímpar (blossom)
            elif pai[u] != v:
                flor = set()
                vertice = u
                while vertice != raiz:
                    flor.add(base[vertice])
                    vertice = pai[vertice]
                vertice = v
                while vertice != raiz:
                    flor.add(base[vertice])
                    vertice = pai[vertice]

                # Contrair a flor
                nova_base = next(iter(flor))
                for vertice in flor:
                    base[vertice] = nova_base
                    if vertice in visitados:
                        visitados.remove(vertice)
                        fila.append(vertice)
                    pai[vertice] = None
    return None

def aumentar_emparelhamento(grafo, emparelhamento, pai, inicio, fim):
    u = fim
    while u is not None:
        v = pai[u]
        proximo_u = emparelhamento[v] if v in emparelhamento else None
        emparelhamento[u] = v
        emparelhamento[v] = u
        u = proximo_u

def algoritmo_blossom(grafo):
    emparelhamento = {}
    for vertice in grafo:
        if vertice not in emparelhamento:
            pai = {}
            fim = encontrar_caminho(grafo, emparelhamento, pai, vertice)
            if fim is not None:
                aumentar_emparelhamento(grafo, emparelhamento, pai, vertice, fim)
    return emparelhamento

# Exemplo de uso
grafo = {
    1: [2, 3],
    2: [1, 3, 4],
    3: [1, 2, 4],
    4: [2, 3, 5],
    5: [4]
}

emparelhamento_maximo = algoritmo_blossom(grafo)
print("Emparelhamento máximo:", emparelhamento_maximo)