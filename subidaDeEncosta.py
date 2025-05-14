def gera_estado_inicial(pesos, capacidade):
    import random
    n = len(pesos)
    estado = [0] * n
    indices = list(range(n))
    random.shuffle(indices)
    for i in indices:
        if sum(pesos[j] for j, sel in enumerate(estado) if sel) + pesos[i] <= capacidade:
            estado[i] = 1
    return estado

def calcula_peso_valor(estado, pesos, valores):
    peso_total = sum(pesos[i] for i, sel in enumerate(estado) if sel)
    valor_total = sum(valores[i] for i, sel in enumerate(estado) if sel)
    return peso_total, valor_total

def gera_vizinhos(estado, pesos, capacidade):
    vizinhos = []
    n = len(estado)
    for i in range(n):
        for j in range(n):
            if i != j and estado[i] != estado[j]:
                novo_estado = estado.copy()
                novo_estado[i] = 1 - novo_estado[i]
                novo_estado[j] = 1 - novo_estado[j]
                peso_total = sum(pesos[k] for k, sel in enumerate(novo_estado) if sel)
                if peso_total <= capacidade:
                    vizinhos.append(novo_estado)
    for i in range(n):
        novo_estado = estado.copy()
        novo_estado[i] = 1 - novo_estado[i]
        peso_total = sum(pesos[k] for k, sel in enumerate(novo_estado) if sel)
        if peso_total <= capacidade:
            vizinhos.append(novo_estado)
    return vizinhos

def melhor_vizinho(estado_atual, pesos, valores, capacidade):
    vizinhos = gera_vizinhos(estado_atual, pesos, capacidade)
    if not vizinhos:
        return estado_atual, * calcula_peso_valor(estado_atual, pesos, valores)
    melhor_estado = None
    melhor_valor = -1
    melhor_peso = 0
    for vizinho in vizinhos:
        peso, valor = calcula_peso_valor(vizinho, pesos, valores)
        if valor > melhor_valor:
            melhor_estado = vizinho
            melhor_valor = valor
            melhor_peso = peso
    return melhor_estado, melhor_peso, melhor_valor

def subida_de_encosta(pesos, valores, capacidade):
    estado_atual = gera_estado_inicial(pesos, capacidade)
    peso_atual, valor_atual = calcula_peso_valor(estado_atual, pesos, valores)
    while True:
        proximo_estado, proximo_peso, proximo_valor = melhor_vizinho(
            estado_atual, pesos, valores, capacidade)
        if proximo_valor <= valor_atual:
            break
        estado_atual = proximo_estado
        peso_atual = proximo_peso
        valor_atual = proximo_valor
    return estado_atual, peso_atual,valor_atual

