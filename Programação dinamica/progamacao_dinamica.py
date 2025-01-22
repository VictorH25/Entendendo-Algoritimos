def mochila_01(itens, capacidade):
    """
    Algoritmo de Programação Dinâmica para o Problema da Mochila.
    - itens: lista de tuplas (valor, peso) dos itens disponíveis.
    - capacidade: a capacidade máxima da mochila.
    """
    # Criar uma tabela para armazenar o valor máximo que pode ser alcançado para cada peso
    n = len(itens)
    tabela = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]
    
    # Preencher a tabela de Programação Dinâmica
    for i in range(1, n + 1):
        for w in range(1, capacidade + 1):
            valor, peso = itens[i - 1]
            if peso <= w:
                tabela[i][w] = max(tabela[i - 1][w], tabela[i - 1][w - peso] + valor)
            else:
                tabela[i][w] = tabela[i - 1][w]
    
    # O valor máximo estará na célula tabela[n][capacidade]
    return tabela[n][capacidade]

# Exemplo de uso
itens = [
    (60, 10),  # (valor, peso)
    (100, 20),
    (120, 30)
]
capacidade = 50  # Capacidade da mochila

valor_maximo = mochila_01(itens, capacidade)

print(f"\nValor máximo que pode ser carregado na mochila: {valor_maximo}")
