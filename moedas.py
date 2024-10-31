def calculaTroco(troco,moedas):
    conjunto_moedas = list()
    #for i in range(len(moedas)):
    #    moedas[i] = moedas[i] * 100    
    moedas = sorted(moedas, reverse=True)
    print(moedas)
    #troco = troco * 100
    for i in moedas:
        print(i)
        while troco >= i:
            conjunto_moedas.append(i)
            troco = troco - i
    #for i in range(len(conjunto_moedas)):
    #    conjunto_moedas[i] = conjunto_moedas[i] / 100
    return conjunto_moedas
        
    



num = 1
moedas = list()
troco = float(input('Digite o troco: '))

moedas = [1,10,25,50]

conjunto = calculaTroco(troco,moedas)

print(f'Conjunto de moedas utilizadas: {conjunto}')