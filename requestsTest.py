import requests

link = "https://api.github.com" 
resposta = requests.get(link)


if resposta.status_code == 200:
    print("Conexão bem-sucedida!")
    dados = resposta.json()
    print(f"Mensagem do servidor: {dados['current_user_url']}")
else:
    print(f"Erro na conexão: {resposta.status_code}")