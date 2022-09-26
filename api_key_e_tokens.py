'''
-------------------------------------- API_KEYS e Tokens -----------------------------------------------

Para acessarmos tais variáveis no nosso programa, instalaremos o pacote python-dotenv na versão 0.19.2
'''
import os
import requests
from dotenv import load_dotenv

#seta o carregamento das variávies de ambiente e permite que as acessamos
load_dotenv()

#A função 'os.environ.get' retorna cada variável e captura o conteúdo das vaiáveis ambiente do arquivo .env  armazenando elas nas variáveis 'API_KEY' e 'TOKEN'
API_KEY = os.environ.get("API_KEY")
TOKEN = os.environ.get("TOKEN")

#Uma sessão permite que tenhamos parâmetros comuns em todas as requisições, sem precisarmos repetí-los.

#Cria a sessão
session = requests.Session()

#Adiciona Parâmetros comuns em todas as requisições
session.params = {
    'key':API_KEY,
    'token':TOKEN
}
#OBS: Para fazermos requisições na sessão que criamos, utilizamos o objeto 'session' ao invés da função requests.get. Por exemplo, uma requisição get seria algo como: session.get('...')

'''Obtendo meus quadros no Trello
'''

# #Parâmetros para ser enviado pela url
# parametros = {
#     #Campos que queremos obter as informações 
#     'fields':['name', 'url']
# }

# #Requisição
# response = session.get(f'https://api.trello.com/1/members/me/boards', params=parametros)

# #Verificação do 'response', se ele retoenar com status 200, será exibido os dados
# if response.status_code == 200:
#     #Lista de dicionário contendo resposta
#     data = response.json()

#     #Percorre a lista de dicionário imprimindo informações 'name', 'url' e 'id'.
#     for board in data:
#         print(f'ID: {[board["id"]]}')
#         print(f'NAME: {[board["name"]]}')
#         print(f'URL: {[board["url"]]}')
#         print('\n')
# else:
#     print('An error occurred, call an adult.')

'''Criando meus quadros no Trello
'''

#Parâmetros da URL

parameters = {
    'name':'Neps API Course',
    'desc':"That's a test board for the Neps API Couse"
}

#Requisição POST - Cria novo quadro com parâmetros especificados acima
response = session.post('https://api.trello.com/1/boards', params=parameters)

#Exibe a resposta se o status for de sucesso, do contrário exibe a mensagem de errro.
if response.status_code == 200:
    # Dados do novo quadro
    data = response.json()

    print(f'Name: {data["name"]}')
    print(f'Description: {data["desc"]}')
    print(f'URL: {data["url"]}')
    print(f'ID: {data["id"]}')
else:
    print('An error occurred, call an adult.')