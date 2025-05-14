import random
import math

def geraEstadoAleatorio(peso, C):
    estado = [random.choice([0, 1]) for _ in peso]
    soma = sum(p for p, ativo in zip(peso, estado) if ativo)
    return estado, soma, -abs(C - soma)  

def geraVizinhoAleatorio(estadoAtual, peso, C, t):
    novoEstado = estadoAtual[:]
    i = random.randint(0, len(peso) - 1)
    novoEstado[i] = 1 - novoEstado[i] 
    novaSoma = sum(p for p, ativo in zip(peso, novoEstado) if ativo)
    return novoEstado, novaSoma, -abs(C - novaSoma)

def geraAgenda(peso, tamanho):
    T0 = 100.0
    fatorResfriamento = 0.95
    return [T0 * (fatorResfriamento ** i) for i in range(tamanho)]

def simulatedAnnealing(peso, C, tamanhoAgenda):
    estadoAtual, somaAtual, valorAtual = geraEstadoAleatorio(peso, C)
    melhorEstado, melhorSoma, melhorValor = estadoAtual, somaAtual, valorAtual
    T = geraAgenda(peso, tamanhoAgenda)

    for t in T:
        vizinhoEstado, vizinhoSoma, vizinhoValor = geraVizinhoAleatorio(estadoAtual, peso, C, t)
        if vizinhoValor > valorAtual:
            estadoAtual, somaAtual, valorAtual = vizinhoEstado, vizinhoSoma, vizinhoValor
            if vizinhoValor > melhorValor:
                melhorEstado, melhorSoma, melhorValor = vizinhoEstado, vizinhoSoma, vizinhoValor
        else:
            if random.random() < math.exp((valorAtual - vizinhoValor) / t):
                estadoAtual, somaAtual, valorAtual = vizinhoEstado, vizinhoSoma, vizinhoValor

    return melhorEstado, melhorSoma, melhorValor
