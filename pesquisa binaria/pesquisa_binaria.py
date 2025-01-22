def pesquisa_binaria(lista, alvo):
    esquerda, direita = 0, len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1

# Exemplo de uso:
lista = [1, 3, 5, 7, 9, 11, 13, 15]
alvo = 7

resultado = pesquisa_binaria(lista, alvo)

if resultado != -1:
    print(f"Elemento encontrado no índice {resultado}.")
else:
    print("Elemento não encontrado na lista.")
