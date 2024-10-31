n = int(input(''))
lista = list()
lista = list(map(int, input().split()))

soma = lista[0]
aux = 0
x=1
if lista[0] < 0:
    x=2
    soma = lista[1]
for i in range(x,len(lista)):
    if soma + lista[i] >= 0:
        soma = lista[i] + soma
    else:
        soma = 0
    if aux < soma:
        aux = soma
 
print(aux)


