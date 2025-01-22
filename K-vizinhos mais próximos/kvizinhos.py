import math

# Dados de treinamento (pontos) e suas classes (rótulos)
treino = [
    [1, 2],  # Ponto 1
    [2, 3],  # Ponto 2
    [3, 3],  # Ponto 3
    [6, 5],  # Ponto 4
    [7, 8],  # Ponto 5
    [8, 8]   # Ponto 6
]
labels = ['A', 'A', 'A', 'B', 'B', 'B']

# Ponto a ser classificado
ponto_a_classificar = [5, 5]

# Número de vizinhos
k = 3

# Calcular a distância Euclidiana entre o ponto a ser classificado e todos os pontos de treinamento
distancias = []
for i in range(len(treino)):
    distancia = math.sqrt(sum((x - y) ** 2 for x, y in zip(treino[i], ponto_a_classificar)))
    distancias.append((distancia, labels[i]))

# Ordenar as distâncias e pegar os k vizinhos mais próximos
distancias.sort(key=lambda x: x[0])  # Ordena pela distância (menor para maior)
vizinhos_k = distancias[:k]

# Contar as classes dos vizinhos
classes = [vizinho[1] for vizinho in vizinhos_k]
classe_mais_comum = max(set(classes), key=classes.count)

print(f"O ponto {ponto_a_classificar} foi classificado como classe '{classe_mais_comum}'.")
