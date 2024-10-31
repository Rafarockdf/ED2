class Edge:
    def __init__(self, v):
        self.v = v
        self.n = None


class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [None] * V
        self.match = [-1] * V
        self.base = list(range(V))
        self.pai = [-1] * V
        self.inQ = [False] * V
        self.inB = [False] * V
        self.q = []
    
    def add_edge(self, u, v):
        edge_u = Edge(v)
        edge_u.n = self.adj[u]
        self.adj[u] = edge_u

        edge_v = Edge(u)
        edge_v.n = self.adj[v]
        self.adj[v] = edge_v

    def LCA(self, root, u, v):
        inP = [False] * self.V
        while True:
            u = self.base[u]
            inP[u] = True
            if u == root:
                break
            u = self.pai[self.match[u]]

        while True:
            v = self.base[v]
            if inP[v]:
                return v
            else:
                v = self.pai[self.match[v]]

    def marca_blossom(self, lca, u):
        while self.base[u] != lca:
            v = self.match[u]
            self.inB[self.base[u]] = self.inB[self.base[v]] = True
            u = self.pai[v]
            if self.base[u] != lca:
                self.pai[u] = v

    def contrai_blossom(self, s, u, v):
        lca = self.LCA(s, u, v)
        self.inB = [False] * self.V
        self.marca_blossom(lca, u)
        self.marca_blossom(lca, v)

        if self.base[u] != lca:
            self.pai[u] = v
        if self.base[v] != lca:
            self.pai[v] = u

        for i in range(self.V):
            if self.inB[self.base[i]]:
                self.base[i] = lca
                if not self.inQ[i]:
                    self.q.append(i)
                    self.inQ[i] = True

    def acha_caminho_aumento(self, s):
        self.inQ = [False] * self.V
        self.pai = [-1] * self.V

        for i in range(self.V):
            self.base[i] = i
        self.q = [s]
        self.inQ[s] = True

        qh = 0
        qt = 1

        while qh < qt:
            u = self.q[qh]
            qh += 1

            for edge in self.iter_edges(u):
                v = edge.v
                if self.base[u] != self.base[v] and self.match[u] != v:
                    if (v == s) or (self.match[v] != -1 and self.pai[self.match[v]] != -1):
                        self.contrai_blossom(s, u, v)
                    elif self.pai[v] == -1:
                        self.pai[v] = u
                        if self.match[v] == -1:
                            return v
                        elif not self.inQ[self.match[v]]:
                            self.q.append(self.match[v])
                            self.inQ[self.match[v]] = True

        return -1

    def aumenta_emparelhamento(self, s, t):
        u = t
        while u != -1:
            v = self.pai[u]
            w = self.match[v]
            self.match[v] = u
            self.match[u] = v
            u = w
        return t != -1

    def edmonds_blossom(self):
        match_new = 0
        for u in range(self.V):
            if self.match[u] == -1:
                match_new += self.aumenta_emparelhamento(u, self.acha_caminho_aumento(u))
        return match_new

    def iter_edges(self, u):
        edge = self.adj[u]
        while edge:
            yield edge
            edge = edge.n


def main():
    V, E = map(int, input("Digite o número de vértices e arestas: ").split())
    graph = Graph(V)

    for _ in range(E):
        u, v = map(int, input("Digite a aresta (u v): ").split())
        u -= 1
        v -= 1
        graph.add_edge(u, v)

    match_size = graph.edmonds_blossom()
    print(f"O tamanho do emparelhamento máximo = {match_size}")

    for v in range(V):
        if v < graph.match[v]:
            print(f"{v+1} está emparelhado com {graph.match[v]+1}")


if __name__ == "__main__":
    main()
