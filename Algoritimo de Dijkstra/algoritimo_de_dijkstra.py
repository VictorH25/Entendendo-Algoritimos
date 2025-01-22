import heapq

def dijkstra(grafo, inicio):
    """
    Algoritmo de Dijkstra para encontrar o caminho mais curto.
    - grafo: dicionário de grafos representado como {nó: [(vizinhos, peso), ...]}.
    - inicio: nó inicial.
    """
    # Inicializando as distâncias com infinito
    distancias = {nó: float('inf') for nó in grafo}
    distancias[inicio] = 0  # Distância do nó inicial é 0

    # Fila de prioridade para explorar os nós com a menor distância
    fila_prioridade = [(0, inicio)]  # (distância, nó)

    while fila_prioridade:
        # Pegando o nó com a menor distância
        distancia_atual, nó_atual = heapq.heappop(fila_prioridade)
        print(f"Explorando o nó {nó_atual} com distância {distancia_atual}")

        # Se a distância encontrada já for maior do que a atual, ignoramos
        if distancia_atual > distancias[nó_atual]:
            continue

        # Verificando os vizinhos
        for vizinho, peso in grafo[nó_atual]:
            nova_distancia = distancia_atual + peso

            # Se encontramos um caminho mais curto
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                heapq.heappush(fila_prioridade, (nova_distancia, vizinho))
    
    return distancias

# Exemplo de uso
grafo = {
    "A": [("B", 1), ("C", 4)],
    "B": [("A", 1), ("C", 2), ("D", 5)],
    "C": [("A", 4), ("B", 2), ("D", 1)],
    "D": [("B", 5), ("C", 1)]
}

inicio = "A"
print(f"Distâncias a partir de {inicio}:")
distancias = dijkstra(grafo, inicio)
print(distancias)
