from time import sleep
alunos = []

while True:
    try:
        dados = {}
        dados['nome'] = str(input('Qual o nome do aluno?  ')).capitalize()
        while True:
            try:
                dados['idade'] = int(input('Qual a idade do aluno? '))
                break
            except ValueError:
                print("Erro: A idade deve ser um número inteiro. Tente Novamente.")
        alunos.append(dados.copy())
        dados.clear()
        while True:
            pergunta = input('Deseja adcionar outro aluno? ').upper()
            if pergunta in ['S', 'N']:
                break
            else:
                print ("Erro: Digite 'S' para Sim e 'N' para Não ")
        if pergunta != 'S':
            break
    except Exception as e:
        print(f'Ocorreu um erro inesperado: {e} ')
        
    
def quicksort(array, chave):
    sleep(1)
    print(array)
    if len(array) < 2:
        return array
    else:
        pivo = array [0]
        menores = [i for i in array [1:] if i[chave] <= pivo[chave]]
        maiores = [i for i in array [1:] if i[chave] > pivo[chave]]
        resultado_ordenacao = quicksort(menores, chave) + [pivo] + quicksort(maiores, chave)
        print (resultado_ordenacao)
        return resultado_ordenacao
    

for aluno in alunos_ordenados:
    print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}")







