import requests

# 1. Fazendo o pedido (Simulando uma chamada de API)
link = "https://api.github.com" # Exemplo usando o GitHub antes da Riot
resposta = requests.get(link)

# 2. Verificando se funcionou
if resposta.status_code == 200:
    print("Conexão bem-sucedida!")
    # Os dados geralmente vêm em formato JSON (parece um dicionário de Python)
    dados = resposta.json()
    print(f"Mensagem do servidor: {dados['current_user_url']}")
else:
    print(f"Erro na conexão: {resposta.status_code}")