def mochila_fracionada(itens, capacidade):
    """
    Algoritmo Guloso para o Problema da Mochila Fracionada.
    - itens: lista de tuplas (valor, peso) dos itens disponíveis.
    - capacidade: a capacidade máxima da mochila.
    """
    # Calcular a razão valor/peso para cada item
    itens_com_valor_por_peso = [(valor, peso, valor/peso) for valor, peso in itens]
    
    # Ordena os itens pela razão valor/peso em ordem decrescente
    itens_com_valor_por_peso.sort(key=lambda x: x[2], reverse=True)

    valor_total = 0  # Valor total da mochila
    peso_total = 0  # Peso total da mochila

    # Iterar sobre os itens, começando pelo de melhor razão valor/peso
    for valor, peso, valor_por_peso in itens_com_valor_por_peso:
        if peso_total + peso <= capacidade:
            # Se o item cabe inteiro na mochila, adicione ele completamente
            valor_total += valor
            peso_total += peso
            print(f"Adicionando item de peso {peso} e valor {valor}.")
        else:
            # Se o item não cabe completamente, adicione a fração dele
            restante = capacidade - peso_total
            valor_total += valor_por_peso * restante
            peso_total += restante
            print(f"Adicionando fração do item de peso {restante} e valor {valor_por_peso * restante}.")
            break  # A mochila está cheia, podemos parar

    return valor_total, peso_total


# Exemplo de uso
itens = [
    (60, 10),  # (valor, peso)
    (100, 20),
    (120, 30)
]
capacidade = 50  # Capacidade da mochila

valor_total, peso_total = mochila_fracionada(itens, capacidade)

print(f"\nValor total na mochila: {valor_total}")
print(f"Peso total na mochila: {peso_total}")
