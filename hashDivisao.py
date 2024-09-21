import random
# 2 * 50 = 100 Tamanho da tabela será 97 porque é o número primo mais próximo de 100
_tamanho=1709
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
            tabela[i].valor = None
            tabela[i].proximo = ListaEncadeada()
        return tabela
    # Continuar implementação
    def inserirTabela(self,tabela,elemento):
        modIndice = sum(ord(caractere) for caractere in elemento) % _tamanho
        if tabela[modIndice].valor == None:
            tabela[modIndice].valor = elemento
        else:
            tabela[modIndice].proximo.inserir(elemento)
            
        
with open(r'cidades.txt', 'r') as arquivo:

    linhas = arquivo.readlines()
    
#linhas_aleatorias = random.sample(linhas, 50)
    
lista_cidades = []
for linha in linhas:
    lista_cidades.append(linha.strip())    
    
tabela_hash = TabelaHash()
tabela = tabela_hash.inicializaTabela(_tamanho)


for cidade in lista_cidades:
    tabela_hash.inserirTabela(tabela,cidade)
colisoes = 0  
 
# Verificar a tabela
for i in range(_tamanho):
    
    if tabela[i].valor is not None:
        print(f"Índice {i}: {tabela[i].valor}")
        no_atual = tabela[i].proximo.inicio
        while no_atual:
            print(f"    Colisão -> {no_atual.chave}")
            no_atual = no_atual.proximo
            colisoes+=1

print(f'A tabela Hash teve {colisoes} colisões')
        