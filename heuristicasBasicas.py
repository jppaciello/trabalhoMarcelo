def soma_peso(subconjunto, pesos):
    return sum(pesos[i] for i in subconjunto)

def first_fit(pesos, valor, n, capacidade):
    subconjunto = []
    for i in range(n):
        if soma_peso(subconjunto, pesos) + pesos[i] <= capacidade:
            subconjunto.append(i)
    return subconjunto

def best_fit(pesos, valor, n, capacidade):
    pp = pesos.copy()
    vv = valor.copy()
    indices = [i for i in range(len(pesos))]
    pp, vv, indices = selection_sort_ratio(pp, vv, indices, True)
    subconjunto = []
    for i in range(n):
        if soma_peso(subconjunto, pp) + pp[i] <= capacidade:
            subconjunto.append(i)
    return [indices[i] for i in subconjunto]

def worst_fit(pesos, valor, n, capacidade):
    pp = pesos.copy()
    vv = valor.copy()
    indices = [i for i in range(len(pesos))]
    pp, vv, indices = selection_sort_ratio(pp, vv, indices, False)
    subconjunto = []
    for i in range(n):
        if soma_peso(subconjunto, pp) + pp[i] <= capacidade:
            subconjunto.append(i)
    return [indices[i] for i in subconjunto]

def selection_sort_ratio(pesos, valores, indices, decrescente=True):
    n = len(pesos)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            ratio_i = valores[max_idx] / pesos[max_idx]
            ratio_j = valores[j] / pesos[j]
            if (decrescente and ratio_j > ratio_i) or (not decrescente and ratio_j < ratio_i):
                max_idx = j
        pesos[i], pesos[max_idx] = pesos[max_idx], pesos[i]
        valores[i], valores[max_idx] = valores[max_idx], valores[i]
        indices[i], indices[max_idx] = indices[max_idx], indices[i]
    return pesos, valores,indices
