import requests

# Simulando o que viria da API da Riot
dados_da_riot = {
    "nome": "Kanek",
    "estatisticas": {
        "farm_total": 150,
        "minutos_jogo": 20
    }
}

# Para acessar o farm, você vai "entrando" nas chaves do dicionário:
farm = dados_da_riot["estatisticas"]["farm_total"]
tempo = dados_da_riot["estatisticas"]["minutos_jogo"]

print(f"O jogador {dados_da_riot['nome']} fez {farm/tempo} de farm por minuto.")