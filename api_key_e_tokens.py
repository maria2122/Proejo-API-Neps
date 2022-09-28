import os
from symbol import parameters
from urllib import response
import requests
from dotenv import load_dotenv

'''
-------------------------------------- API_KEYS e Tokens : Requests With Security-----------------------------------------------

Para acessarmos tais variáveis no nosso programa, instalaremos o pacote python-dotenv na versão 0.19.2
'''

#1)seta o carregamento das variávies de ambiente e permite que as acessamos
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

#2) Obtendo meus quadros no Trello
def getBoardTrello():
#Parâmetros para ser enviado pela url
    parameters  = {
        #Campos que queremos obter as informações 
        'fields':['name', 'url','idBoard']
    }

    #Requisição
    response = session.get(f'https://api.trello.com/1/members/me/boards', params=parameters )

    #Verificação do 'response', se ele retoenar com status 200, será exibido os dados
    if response.status_code == 200:
        #Lista de dicionário contendo resposta
        data = response.json()

        #Percorre a lista de dicionário imprimindo informações 'name', 'url' e 'id'.
        for board in data:
            print(f'ID: {[board["id"]]}')
            print(f'NAME: {[board["name"]]}')
            print(f'URL: {[board["url"]]}')
            print('\n')
    else:
        print('An error occurred, call an adult.')

#3) Criando meus quadros no Trello
def createBoardTrello():
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

#4) Criando lista no quadro criado
def createListInBoard():
    parameters  = {
        #Campos que queremos obter as informações 
        'name':'List number 2',
        'idBoard':'6331945367d85704f403f56a',
    }

    #Requisição POST
    response = session.post('https://api.trello.com/1/lists/', params=parameters )

    if response.status_code == 200:
        #Dados da lista criada
        data = response.json()

        #imprimindo informações 'name', 'id' e 'idBoard'.
        
        print(f'List name: {data["name"]}')
        print(f'ID: {data["id"]}')
        print(f'ID_Quadro: {data["idBoard"]}')
    else:
        print('An error occurred, call an adult.')

#5) Adicionando um cartão na lista criada
def addCardInList():
    parameters = {
        'name':'Second Card in To Do List',
        'desc':"That's a card for testing in List number 2",
        'idList':'633362cb3f83b602ee5d7da5'
    }

    #Requisição POST
    response = session.post('https://api.trello.com/1/cards',params=parameters)

    if response.status_code == 200:
        #Dados do cartão criado
        data = response.json()

        print(f'Card name: {data["name"]}')
        print(f'ID: {data["id"]}')
        print(f'Description: {data["desc"]}')
    else:
        print('An error occurred, call an adult.')

#6) Editando um Cartão 
def editCard():
    parameters = {
        'name': 'Edited Card number 2',
        'desc': "That' card a test to edit"
    }

    #Requisição POST
    response = session.put('https://api.trello.com/1/cards/633365e3aaea1103e2169687', params=parameters)

    if response.status_code == 200:
        #Dados do card depois da alteração
        data = response.json()
        print(f'Card name: {data["name"]}')
        print(f'ID: {data["id"]}')
        print(f'Description: {data["desc"]}')
    else:
        print('An error occurred, call an adult.')

#7) Deletando um cartão 
def deleteCard():
    parameters = {
        'idList':'633362cb3f83b602ee5d7da5'
    }
    response = session.delete('https://api.trello.com/1/cards/633365e3aaea1103e2169687', params=parameters)

    if response.status_code == 200:
        print('Deleted with successful')
    else:
        print('An error occurred, call an adult.')
