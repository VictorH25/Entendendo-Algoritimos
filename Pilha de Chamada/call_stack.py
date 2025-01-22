def soma_com_pilha(n):
    """
        Calcula a soma dos números de 1 até n usando uma pilha de chamadas explícita.
    """
    if n < 0:
        raise ValueError("A soma não é definida para números negativos.")

    # Pilha para armazenar os números
    pilha = []
    soma = 0

    # Empilhar os números de 1 até n
    for i in range(1, n + 1):
        pilha.append(i)

    # Desempilhar e somar
    while pilha:
        soma += pilha.pop()

    return soma

# Interação com o usuário
while True:
    try:
        numero = int(input("Digite um número inteiro para calcular a soma: "))
        if numero < 0:
            print("A soma não é definida para números negativos. Tente novamente.")
        else:
            break
    except ValueError:
        print("Erro: Digite um número inteiro válido.")

# Calcula e exibe o resultado
resultado = soma_com_pilha(numero)
print(f"A soma dos números de 1 até {numero} é: {resultado}")
