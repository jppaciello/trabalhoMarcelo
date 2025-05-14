
def calcula_soma(subconjunto, numeros, soma_alvo):
    soma = 0
    for num in subconjunto:
        soma += num
        print(soma)
    return soma if soma <= soma_alvo else -1

numeros = [2, 4, 6, 8]
subconjunto = [2, 6]
soma_alvo = 10
calcula_soma(subconjunto,numeros,soma_alvo)
