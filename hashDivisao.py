# 2 ** 10 = 20 Tamanho da tabela será 19 porque é o número primo mais próximo de 10
_tamanho=19
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

# Calasse Tabela Hash
class TabelaHash:
    _tamanho=19
    
    def __init__(self): # Metodo que instancia a classe
        self.indice = None
        self.valor = None
        self.proximo = ListaEncadeada()
    
    def criarTabela(self,tamanho):
        tabela = []  
        for i in range(tamanho):
            tabela.append(TabelaHash())
        return tabela
    
    def inicializaTabela(self,tamanho):
        tabela = self.criarTabela(tamanho)  
        for i in range(tamanho):
            tabela[i].indice = i
            tabela[i].valor = 0
            tabela[i].proximo = ListaEncadeada()
        return tabela
    # Continuar implementação
    def inserirTabela(tabela,elemento):
        x=0
        modIndice = [ord(caractere) for caractere in elemento]
        for i in modIndice:
            x += i
        return x % 13