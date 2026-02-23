import requests

dados_da_riot = {
    "nome": "Kanek",
    "estatisticas": {
        "farm_total": 150,
        "minutos_jogo": 20
    }
}

farm = dados_da_riot["estatisticas"]["farm_total"]
tempo = dados_da_riot["estatisticas"]["minutos_jogo"]

print(f"O jogador {dados_da_riot['nome']} fez {farm/tempo} de farm por minuto.")