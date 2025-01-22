from time import sleep

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

# Interação com o usuário:
valores = []
while True:
    try:
        while True:
            try:
                numero = int(input("Digite um número inteiro para adicionar à lista ordenada (ou -1 para terminar): "))
                if numero == -1:
                    break
                valores.append(numero)
            except ValueError:
                print("Erro: Digite um número inteiro válido.")
        break
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

valores.sort()  # Ordena a lista automaticamente
print(f"Lista ordenada: {valores}")

while True:
    try:
        alvo = int(input("Digite o número que deseja buscar na lista: "))
        break
    except ValueError:
        print("Erro: Digite um número inteiro válido.")

print("Iniciando pesquisa binária...")
sleep(1)
resultado = pesquisa_binaria(valores, alvo)

if resultado != -1:
    print(f"Elemento encontrado no índice {resultado}.")
else:
    print("Elemento não encontrado na lista.")
