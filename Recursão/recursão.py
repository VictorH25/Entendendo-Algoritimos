def fatorial(n):
    """
        Calcula o fatorial de um número usando recursão.
    """
    if n == 0 or n == 1:  # Caso base
        return 1
    return n * fatorial(n - 1)  # Chamada recursiva


while True:
    try:
        numero = int(input("Digite um número inteiro para calcular o fatorial: "))
        if numero < 0:
            print("O fatorial não é definido para números negativos. Tente novamente.")
        else:
            break
    except ValueError:
        print("Erro: Digite um número inteiro válido.")
resultado = fatorial(numero)
print(f"O fatorial de {numero} é: {resultado}")
