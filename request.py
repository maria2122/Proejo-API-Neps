import json
import requests

#Com a biblioteca 'REQUESTS' basta chamá-la passando a URL e parâmetros da API(para get é opcional), no caso eu o 'params' especificamos que queremos a resposta em json
response = requests.get('http://numbersapi.com/22/math', params='json')

#Recebe o status da requisição e compara se esse é 200 de Ok ou 404 de Não encontrada
# status_code = response.status_code
# if(status_code==200):
#     print("Resposta Ok!")
# elif(status_code==404):
#     print("Rota não encontrada :(")


# print(f'Text: {response.text}')
# print(f'Status Code: {response.status_code}')

''' Retorno
Resposta Ok!
Text: {
 "text": "22 is an even composite number, its proper divisors being 1, 2 and 11.",
 "number": 22,
 "found": true,
 "type": "math"
}
'''
#Captura a URL depois de feita a requisição
print(f'URL: {response.url}')

#JSON da resposta
json = response.json()
print(f'Tipo: {type(json)}')
print(f'Dados: {json}')

'''Retorno
URL: http://numbersapi.com/22/math?json
Tipo: <class 'dict'>
Dados: {'text': '22 is the number of partitions of 8.', 'number': 22, 'found': True, 'type': 'math'}
'''