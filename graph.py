# import dice

from matplotlib import pyplot as plt

from itertools import product

import statistics

def DiceGraph(lados):
    x = list(range(1, lados + 1))
    probabilidade = (1/lados) * 100
    y = [probabilidade]
    plt.bar(x,y)
    plt.xlabel("Valores")
    plt.ylabel("Probabilidade")
    plt.title(f'Resultados em gráfico de um dado 1d{lados}')
    plt.xticks(x)

    plt.show()

  

def twoDiceGraph(lados):
    somas = []
    for dado1 in range(1, lados + 1):
        for dado2 in range(1, lados + 1):
            somas.append(dado1 + dado2)

    resultados_possiveis = list(range(2, (lados * 2) + 1))
    contagem = []
    
    for s in resultados_possiveis:
        qtd = somas.count(s)
        porcentagem = (qtd / len(somas)) * 100
        contagem.append(porcentagem)

   
    plt.bar(resultados_possiveis, contagem)
    plt.xlabel('Soma dos Dados')
    plt.ylabel('Probabilidade (%)')
    plt.title(f'Distribuição de Probabilidade para 2d{lados}')
    plt.xticks(resultados_possiveis)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.show()

def DiceRoll(lados,dados):
    somas = []

    match dados:
        case 1:
            DiceGraph(lados)
        case 2:
            twoDiceGraph(lados)
        case 3:
            for dado1 in range(1, lados + 1):
                for dado2 in range(1, lados + 1):
                        for dado3 in range(1, lados + 1):
                            somas.append(dado1 + dado2 + dado3)

    resultados_possiveis = list(range(2, (lados * 3) + 1))
    contagem = []
    
    for s in resultados_possiveis:
        qtd = somas.count(s)
        porcentagem = (qtd / len(somas)) * 100
        contagem.append(porcentagem)

   
    plt.bar(resultados_possiveis, contagem)
    plt.xlabel('Soma dos Dados')
    plt.ylabel('Probabilidade (%)')
    plt.title(f'Distribuição de Probabilidade para 3d{lados}')
    plt.xticks(resultados_possiveis)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.show()

def AnyDiceRoll(dados, lados):
    faces = range(1, lados + 1)
    combinacoes = product(faces, repeat=dados)
    
    somas = []
    for c in combinacoes:
        somas.append(sum(c))

    mediana = statistics.median(somas)
    print(f"Mediana: {mediana}")
        
    menor_soma = dados
    maior_soma = dados * lados
    eixo_x = list(range(menor_soma, maior_soma + 1))
    
    eixo_y = []
    total_combinacoes = lados ** dados
    
    for s in eixo_x:
        qtd = somas.count(s)
        porcentagem = (qtd / total_combinacoes) * 100
        eixo_y.append(porcentagem)
    


    fig, ax = plt.subplots() 
    ax.plot(eixo_x, eixo_y)
    plt.bar(eixo_x, eixo_y, color='mediumpurple', edgecolor='black')
    plt.title(f'Probabilidades para {dados}d{lados}. Valor médio: {mediana}')
    plt.xlabel('Soma dos Resultados')
    plt.ylabel('Probabilidade (%)')
    plt.grid(axis='y', alpha=0.3)
    plt.xticks(somas)
    plt.show()



