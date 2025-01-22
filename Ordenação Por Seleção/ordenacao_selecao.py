from time import sleep

def ordenacao_selecao(lista):
    """
        Ordenação por Seleção:
        Ordena a lista em ordem crescente e exibe a lista após cada troca.
    """
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        # Troca os elementos
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
        
        # Exibe a lista a cada iteração para visualizar a mudança
        print(f"Passo {i+1}: {lista}")
        sleep(1)  # Pausa para visualizar a ordenação

# Interação com o usuário:
valores = []
while True:
    try:
        while True:
            try:
                numero = int(input("Digite um número inteiro para adicionar à lista (ou -1 para terminar): "))
                if numero == -1:
                    break
                valores.append(numero)
            except ValueError:
                print("Erro: Digite um número inteiro válido.")
        break
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Exibe a lista antes da ordenação
print(f"Lista inicial: {valores}")

# Ordenação por Seleção
ordenacao_selecao(valores)

# Exibe a lista final após a ordenação
print(f"Lista ordenada: {valores}")
