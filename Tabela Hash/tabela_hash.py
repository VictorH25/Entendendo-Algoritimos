# Criando a tabela hash como uma lista simples
tabela_hash = [None] * 5  # Tabela com 5 espaços

def calcular_indice(chave):
    """
    Calcula o índice da tabela para uma chave.
    """
    return sum(ord(c) for c in chave) % len(tabela_hash)

def inserir(chave, valor):
    """
    Insere um valor na tabela hash.
    """
    indice = calcular_indice(chave)
    if tabela_hash[indice] is None:
        tabela_hash[indice] = []  # Inicializa uma lista no índice, se necessário
    for par in tabela_hash[indice]:  # Verifica se a chave já existe
        if par[0] == chave:
            par[1] = valor  # Atualiza o valor se a chave já existir
            return
    tabela_hash[indice].append([chave, valor])  # Adiciona a chave-valor

def buscar(chave):
    """
    Busca um valor pela chave na tabela hash.
    """
    indice = calcular_indice(chave)
    if tabela_hash[indice] is not None:
        for par in tabela_hash[indice]:
            if par[0] == chave:
                return par[1]
    return None  # Retorna None se a chave não for encontrada

def remover(chave):
    """
    Remove um valor pela chave da tabela hash.
    """
    indice = calcular_indice(chave)
    if tabela_hash[indice] is not None:
        for par in tabela_hash[indice]:
            if par[0] == chave:
                tabela_hash[indice].remove(par)  # Remove o par
                return True
    return False  # Retorna False se a chave não for encontrada

# Inserir valores
print("Inserindo valores...")
inserir("nome", "Alice")
inserir("idade", "25")
inserir("cidade", "Rio de Janeiro")

# Buscar valores
print("\nBuscando valores...")
print("Nome:", buscar("nome"))
print("Idade:", buscar("idade"))
print("Cidade:", buscar("cidade"))

# Remover valor
print("\nRemovendo 'idade'...")
if remover("idade"):
    print("Idade removida.")
else:
    print("Idade não encontrada.")

# Buscar após remoção
print("\nBuscando 'idade' após remoção...")
print("Idade:", buscar("idade"))
