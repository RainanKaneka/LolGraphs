from matplotlib import pyplot as plt

from itertools import product

import statistics

def graphLolFarm():
    minutos = list(range(0, 10))
    farm_perfeito = [m * 10 for m in minutos]
    media_ouro = [m * 6 for m in minutos]

    farm_real = [0, 6, 15, 25, 32, 45, 50, 58, 65, 70, 75, 82, 88, 92, 95, 105, 115, 125, 135, 145, 150, 158, 169, 181, 191, 206, 214, 230, 249, 256]

    plt.plot(minutos, farm_perfeito, label='Farm Perfeito (10 CS/min)', color='gray', linestyle='--')
    plt.plot(minutos, farm_real, label='Seu Farm Real', color='blue', marker='o')
    plt.plot(minutos,media_ouro, label='Ouro médio', color='yellow', marker='o')

    plt.title('Análise de Desempenho: Farm por Minuto')
    plt.xlabel('Tempo de Jogo (min)')
    plt.ylabel('Total de Farm (CS)')
    plt.legend() 
    plt.grid(True, alpha=0.3)
    plt.show()



def graphLolKill():
    minutos = list(range(1, 10 + 1))
    killPlatina = [k * 0.5 for k in minutos]
    myKills = [0, 1, 1, 3, 3, 5, 6, 8, 8, 9]

    plt.plot(minutos, killPlatina, label='Kill média no Ouro (0.5 Kill/min)', color='gray', linestyle='--' )
    plt.plot(minutos, myKills,label='Seu Farm Real', color='red', marker='o' )

    plt.title('Análise de Desempenho: Kill por Minuto')
    plt.xlabel('Tempo de Jogo (min)')
    plt.ylabel('Total de Kills')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


graphLolKill()

