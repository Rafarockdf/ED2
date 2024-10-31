lista = list()

lista.insert(1,{'1':6})
lista.insert(0,{'1':6})
lista.insert(2,{'2':10})
print(lista)


for i in range(len(lista)):
    for j in lista[i]:
        print(f'-> {j} peso {lista[i][j]}')