import json
from urllib import response
import requests

# # #1) Com a biblioteca 'REQUESTS' basta chamá-la passando a URL e parâmetros da API(para get é opcional), no caso eu o 'params' especificamos que queremos a resposta em json
response = requests.get('http://numbersapi.com/22/math', params='json')

# #Recebe o status da requisição e compara se esse é 200 de Ok ou 404 de Não encontrada
status_code = response.status_code
if(status_code==200):
    print("Resposta Ok!")
elif(status_code==404):
    print("Rota não encontrada :(")


print(f'Text: {response.text}')
print(f'Status Code: {response.status_code}')

# ''' Resposta
# Resposta Ok!
# Text: {
#  "text": "22 is an even composite number, its proper divisors being 1, 2 and 11.",
#  "number": 22,
#  "found": true,
#  "type": "math"
# }
# '''

# #2) Captura a URL depois de feita a requisição
print(f'URL: {response.url}')

# #JSON da resposta
json = response.json()
print(f'Tipo: {type(json)}')
print(f'Dados: {json}')

# '''Resposta
# URL: http://numbersapi.com/22/math?json
# Tipo: <class 'dict'>
# Dados: {'text': '22 is the number of partitions of 8.', 'number': 22, 'found': True, 'type': 'math'}
# '''

# #3) Se quisermos enviar vários parâmetros pela URL basta criar um dicionário e passar ele na requisição

parametros = {'key1':'value1','key2':'value2'}

# #Requisição 'apenas teste'
response = requests.get('https://www.test.com/', params=parametros)
print(response.url)

# #4) Lendo um número e passando na requisição.
number = int(input('Entre com um número'))

# # #Requisição
response = requests.get(f'http://numbersapi.com/{number}/math', params='json')

# Verifica se o status da resposta é válida
if(response.status_code == 200):
    #Dicionário contendo os dados da resposta
    data = response.json()
    #Verifica se a requisição foi encontrada
    if(data['found']==True):
        print(data['text'])
    else:
        print('Desculpe, rota nao encontrada.')
else:
    print('URL invalida.')

'''Resposta:
1 is also the first and second numbers in the Fibonacci sequence and is the first number in many other mathematical sequences.
'''
#5) Enviando dados pelo corpo da requisição com POST com a API https://jsonplaceholder.typicode.com/

#Dicionário contendo os parâmetros para envio no corpo da requisição(modelo JSON)
data = {
    "title": "Esse eh o meu POST",
    "body": "Esse eh o corpo da requisicao",
    "userID": 1
}

# # #Requisição
response = requests.post('https://jsonplaceholder.typicode.com/posts/', json=data)

# #Informações da resposta
print(f'Status Code: {response.status_code}')
print(f'Dados: {response.json()}')

'''Resposta:
Status Code: 201
Dados: {'title': 'Esse eh o meu POST', 'body': 'Esse eh o corpo da requisicao', 'userID': 1, 'id': 101}
'''
# #6) Atualizando recurso (método PUT)
response = requests.put('https://jsonplaceholder.typicode.com/posts/1', json = data)
print(f'Status Code: {response.status_code}')
print(f'Dados: {response.json()}')

'''Resposta:
Status Code: 200
Dados: {'title': 'Esse eh o meu POST', 'body': 'Esse eh o corpo da requisicao', 'userID': 1, 'id': 1}
'''
# #7) Deletando recurso (método DELETE)
response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print(f'Status Code: {response.status_code}')
print(f'Dados: {response.json()}')

'''Resposta:
Status Code: 200
Dados: {}
'''

