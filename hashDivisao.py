import random
from time import time
<<<<<<< HEAD
# 2 * 853 = 1703 Tamanho da tabela será 1709 porque é o número primo mais próximo de 1703
=======
# 2 * 853 = 1703 Tamanho da tabela será 1709 porque é o número primo mais próximo de 1703_tamanho=1709
>>>>>>> 1b51d78bf3e6d3946597c853e33c56438887bdb4
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
        self.tamanhoLista = 0
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
            self.tamanhoLista = 0
            tabela[i].proximo = ListaEncadeada()
        return tabela
    # Continuar implementação
    def inserirTabela(self,tabela,elemento):
        modIndice = int(''.join(str(ord(c)) for c in elemento)) % _tamanho
        if tabela[modIndice].valor == None:
            tabela[modIndice].valor = elemento
        else:
            tabela[modIndice].proximo.inserir(elemento)
            tabela[modIndice].tamanhoLista+=1
        
with open(r'C:\Users\rafam\Desktop\ED2\ED2\cidades.txt', 'r') as arquivo:

    lista_cidades = arquivo.readlines()
    
tabela_hash = TabelaHash()
tabela = tabela_hash.inicializaTabela(_tamanho)

inicio = time()
for cidade in lista_cidades:
    tabela_hash.inserirTabela(tabela,cidade)
fim = time()

colisoes = 0  
maior = 0
# Verificar a tabela
for i in range(_tamanho):
    
    if tabela[i].valor is not None:
        print(f"Índice {i}: {tabela[i].valor}")
        no_atual = tabela[i].proximo.inicio
        while no_atual:
            print(f"    Colisão -> {no_atual.chave}")
            no_atual = no_atual.proximo
            colisoes+=1
for i in range(_tamanho):
    if tabela[i].tamanhoLista > maior:
        maior = tabela[i].tamanhoLista

print(f'A maior lista é {maior}')
print(f'A tabela Hash teve {colisoes} colisões')
    
print(f'Tempo de execução: {fim - inicio}segundos \n')   