from collections import deque

def bfs(grafo, inicio, objetivo):
    """
    Realiza a pesquisa em largura (BFS) em um grafo.
    - grafo: dicionário representando o grafo (nós e arestas).
    - inicio: nó inicial.
    - objetivo: nó que queremos encontrar.
    """
    fila = deque([inicio])  # Fila para armazenar os nós a serem explorados
    visitados = set()  # Conjunto para rastrear nós já visitados

    while fila:
        # Remove o próximo nó da fila
        no_atual = fila.popleft()
        print(f"Explorando: {no_atual}")

        # Verifica se encontramos o objetivo
        if no_atual == objetivo:
            print(f"Nó objetivo '{objetivo}' encontrado!")
            return True

        # Marca o nó como visitado
        visitados.add(no_atual)

        # Adiciona os vizinhos do nó atual na fila, se não visitados
        for vizinho in grafo.get(no_atual, []):
            if vizinho not in visitados:
                fila.append(vizinho)

    print(f"Nó objetivo '{objetivo}' não encontrado no grafo.")
    return False

# Exemplo de uso
grafo = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

print("Grafo:", grafo)

inicio = "A"
objetivo = "F"

print("\nIniciando pesquisa em largura...")
bfs(grafo, inicio, objetivo)
