import random
from time import time
# 2 * 853 = 1703 Tamanho da tabela será 1709 porque é o número primo mais próximo de 1703
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
    _tamanho=103
    
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
            tabela[i].proximo = ListaEncadeada()
            self.tamanhoLista = 0
        return tabela

    def funcao_meio_quadrado(self, chave):
        # Calcula o quadrado da chave e extrai o meio
        chave = int(''.join(str(ord(c)) for c in chave))  # Converte a chave para um número
        quadrado = chave ** 2
        quadrado_str = str(quadrado)
        meio = len(quadrado_str) // 2
        meio_quadrado = quadrado_str[meio - 2:meio + 2]  # Extrai 4 dígitos centrais
        return int(meio_quadrado) % _tamanho

    def inserirTabela(self, tabela, elemento):
        modIndice = self.funcao_meio_quadrado(elemento)
        if tabela[modIndice].valor is None:
            tabela[modIndice].valor = elemento
        else:
            tabela[modIndice].proximo.inserir(elemento)
            tabela[modIndice].tamanhoLista +=1
    
        
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
            colisoes += 1
for i in range(_tamanho):
    if tabela[i].tamanhoLista > maior:
        maior = tabela[i].tamanhoLista

print(f'A maior lista é {maior}')
print(f'A tabela Hash teve {colisoes} colisões')

print(f'Tempo de execução: {fim - inicio}segundos \n')       