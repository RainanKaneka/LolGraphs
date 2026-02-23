import requests

from matplotlib import pyplot as plt

from itertools import product

def buscar_perfil_lol(game_name, tag_line, api_key):
    # A Riot usa 'endpoints' diferentes. Este é para converter nome e tag em um PUUID (ID único)
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
MEU_NOME = "Frierelia" # Coloque seu nome sem a tag
MINHA_TAG = "elfa"   # Coloque apenas o que vem depois do #

buscar_perfil_lol(MEU_NOME,MINHA_TAG, MINHA_CHAVE)


def buscar_lista_partidas(puuid, api_key):
    # Agora usamos a rota de MATCH (partidas)
    # Vamos pegar as últimas 5 partidas para testar
    url_partidas = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=10"
    
    headers = {"X-Riot-Token": api_key}
    resposta = requests.get(url_partidas, headers=headers)

    if resposta.status_code == 200:
        lista_ids = resposta.json()
        print(f"IDs das últimas partidas: {lista_ids}")
        return lista_ids
    else:
        print(f"Erro ao buscar partidas: {resposta.status_code}")
        return None

# Use o PUUID que apareceu no seu terminal
MEU_PUUID = "eoQSMKyD5ePidEJQD8Gnm406Dhb0PiU8TdDZ2e_ZSEDQj4FmRmhg-BKw8J4elYmDnP5xplG4enlMLA" 
buscar_lista_partidas(MEU_PUUID, MINHA_CHAVE)

def buscar_detalhes_partida(match_id, meu_puuid, api_key):
    # Rota para detalhes de UMA partida específica
    url_detalhes = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}"
    
    headers = {"X-Riot-Token": api_key}
    resposta = requests.get(url_detalhes, headers=headers)

    if resposta.status_code == 200:
        partida = resposta.json()
        
        # O JSON da partida é ENORME. Precisamos encontrar VOCÊ entre os 10 jogadores.
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


# Testando com o primeiro ID da sua lista
lista_ids = ['BR1_3209656288', 'BR1_3209640040', 'BR1_3209598102', 'BR1_3209515621', 'BR1_3209503547'] # Coloque aqui a lista que apareceu no seu terminal

API_KEY = "RGAPI-cbbd0be6-e747-42a7-9d60-12d9f3daee11"
NOME = "Ghostfan"
TAG = "ghost"

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
    
    duracao_segundos = dados_partida['info']['gameDuration']
    minutos_totais = int(duracao_segundos / 60)
    
    participantes = dados_partida['info']['participants']
    meu_farm = 0
    for p in participantes:
        if p['puuid'] == puuid:
            meu_farm = p['totalMinionsKilled'] + p['neutralMinionsKilled']
            break

    for jogador in participantes:
            if jogador['puuid'] == puuid:
                print(f"Partida encontrada! Duração: {minutos_totais:.2f} min")
                print(f"Seu Farm Total: {meu_farm} CS")
                print(f"Média: {meu_farm/minutos_totais:.1f} CS/min")
                
                # return meu_farm, minutos_totais       

    tempo = list(range(0, minutos_totais + 1))
    
    farm_perfeito = [t * 10 for t in tempo]
    
    seu_farm_progresso = [ (t / minutos_totais) * meu_farm for t in tempo]

    plt.figure(figsize=(10, 6))
    plt.plot(tempo, farm_perfeito, label='Meta: 10 CS/min', color='gray', linestyle='--')
    plt.plot(tempo, seu_farm_progresso, label=f'Seu Farm Real ({meu_farm} CS)', color='blue', linewidth=2)
    
    plt.title(f'Desempenho de Farm - Partida {match_id}')
    plt.xlabel('Tempo (minutos)')
    plt.ylabel('Quantidade de Minions (CS)')
    plt.legend()
    plt.grid(True, alpha=0.2)
    
    print(f"Gráfico gerado para a partida {match_id}!")
    plt.show()

script_completo_lol()

