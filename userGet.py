import requests

from matplotlib import pyplot as plt

from itertools import product

def buscar_perfil_lol(game_name, tag_line, api_key):
    url_conta = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    
    headers = {
        "X-Riot-Token": api_key
    }

    resposta = requests.get(url_conta, headers=headers)

    if resposta.status_code == 200:
        dados = resposta.json()
        print(f"Sucesso! Encontramos o jogador: {dados['gameName']}#{dados['tagLine']}")
        print(f"Seu PUUID é: {dados['puuid']}")
        return dados['puuid']
    else:
        print(f"Erro na conexão: {resposta.status_code}")
        print("Verifique se sua API Key é válida ou se o Nome#Tag estão corretos.")
        return None

MINHA_CHAVE = "RGAPI-cbbd0be6-e747-42a7-9d60-12d9f3daee11"
MEU_NOME = "Frierelia" 
MINHA_TAG = "elfa"   

buscar_perfil_lol(MEU_NOME,MINHA_TAG, MINHA_CHAVE)


def buscar_lista_partidas(puuid, api_key):

    url_partidas = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=5"
    
    headers = {"X-Riot-Token": api_key}
    resposta = requests.get(url_partidas, headers=headers)

    if resposta.status_code == 200:
        lista_ids = resposta.json()
        print(f"IDs das últimas partidas: {lista_ids}")
        return lista_ids
    else:
        print(f"Erro ao buscar partidas: {resposta.status_code}")
        return None

MEU_PUUID = "eoQSMKyD5ePidEJQD8Gnm406Dhb0PiU8TdDZ2e_ZSEDQj4FmRmhg-BKw8J4elYmDnP5xplG4enlMLA" 
buscar_lista_partidas(MEU_PUUID, MINHA_CHAVE)

def buscar_detalhes_partida(match_id, meu_puuid, api_key):
    url_detalhes = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}"
    
    headers = {"X-Riot-Token": api_key}
    resposta = requests.get(url_detalhes, headers=headers)

    if resposta.status_code == 200:
        partida = resposta.json()
        participantes = partida['info']['participants']
        
        for jogador in participantes:
            if jogador['puuid'] == meu_puuid:
                farm = jogador['totalMinionsKilled'] + jogador['neutralMinionsKilled']
                tempo_minutos = partida['info']['gameDuration'] / 60
                
                print(f"Partida encontrada! Duração: {tempo_minutos:.2f} min")
                print(f"Seu Farm Total: {farm} CS")
                print(f"Média: {farm/tempo_minutos:.1f} CS/min")
                
                return farm, tempo_minutos
    else:
        print(f"Erro ao buscar detalhes: {resposta.status_code}")
        return None


    tempo = list(range(0, tempo_minutos + 1))
    farm_perfeito = [t * 10 for t in tempo]
    seu_farm_progresso = [ (t / tempo_minutos) * meu_farm for t in tempo]


    plt.figure(figsize=(10, 6))
    plt.plot(tempo, farm_perfeito, label='Meta: 10 CS/min', color='gray', linestyle='--')
    plt.plot(tempo, meu_farm, label=f'Seu Farm({meu_farm} CS)', color='blue', linewidth=2)
    plt.title(f'Análise de Desempenho: Farm por Minuto, Partida {match_id}')
    plt.xlabel('Tempo de Jogo (min)')
    plt.ylabel('Total de Farm')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


lista_ids = ['BR1_3209656288', 'BR1_3209640040', 'BR1_3209598102', 'BR1_3209515621', 'BR1_3209503547']


#------------------ Script de FARM/Min da sua ULTIMA partida no LOL ------------------------


API_KEY = "RGAPI-cbbd0be6-e747-42a7-9d60-12d9f3daee11"
NOME = input("Digite o seu nome: ")
TAG = input("Digite sua tag (Sem a hashtag): ")

def script_completo_lol():
    url_conta = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{NOME}/{TAG}"
    headers = {"X-Riot-Token": API_KEY}
    
    res_perfil = requests.get(url_conta, headers=headers)
    if res_perfil.status_code != 200:
        print("Erro ao achar perfil. Verifique a chave!")
        return
    
    puuid = res_perfil.json()['puuid']
    
    url_partidas = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=1"
    match_id = requests.get(url_partidas, headers=headers).json()[0]
    
    url_detalhes = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}"
    dados_partida = requests.get(url_detalhes, headers=headers).json()

    url_timeline = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline"
    resposta_timeline = requests.get(url_timeline, headers=headers)

    if resposta_timeline.status_code == 200:
        timeline = resposta_timeline.json()
        frames = timeline['info']['frames']
        duracao_segundos = dados_partida['info']['gameDuration']
        # minutos_totais = int(duracao_segundos / 60)
        minutos_lista = []
        farm_min_lista = []

        participantes = timeline['info']['participants']
        meu_id = None
        for p in participantes:
            if p['puuid'] == puuid:
                meu_id = p['participantId']
                break

        if meu_id is None:
            print("Erro: Não foi possível encontrar seu participante na partida.")
            return None, None            

        for i, frame in enumerate(frames):
            meus_dados_neste_minuto = frame['participantFrames'][str(meu_id)]
            farm_atual = meus_dados_neste_minuto['minionsKilled'] + meus_dados_neste_minuto['jungleMinionsKilled'
            minutos_lista.append(i) 
            farm_min_lista.append(farm_atual)
    else:
        print(f"Erro ao buscar a timeline: {resposta.status_code}")
        return None, None
    
    farm_perfeito = [t * 10 for t in minutos_lista]

    total_farm = farm_min_lista[-1]
    

    plt.figure(figsize=(10, 6))
    plt.plot(minutos_lista, farm_perfeito, label='Meta: 10 CS/min', color='gold', linestyle='--')
    plt.plot(minutos_lista, farm_min_lista, label=f'Seu Farm Real ({total_farm} CS)', color='blue', marker='o', linewidth=2)
    
    plt.title(f'Desempenho de Farm de {NOME} - Partida {match_id}')
    plt.xlabel('Tempo (minutos)')
    plt.ylabel('Quantidade de Minions (CS)')
    plt.legend()
    plt.grid(True, alpha=0.2)
    print(f"Gráfico gerado para a partida {match_id}!")
    plt.show()

script_completo_lol()
