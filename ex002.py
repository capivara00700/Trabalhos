#Importando a biblioteca AwesomeAPI, para obter a cotação das moedas em tempo real
import requests

response = requests.get("https://economia.awesomeapi.com.br/last/USD,EUR,BTC")
data = response.json()

#Dando boas vinda e perguntando qual função o usuario deseja acessar
print('Olá, seja bem vindo ao meu projeto de conversão de moedas!!')
print('1. Conversor de moedas \n2. Cotação das moedas')
cc = input("Primerio escolha uma das opções (colocar apenas o numero): ")

if cc == "1" or cc == "conversor de moedas":
  print('1. Dólar \n2. Euro \n3. Bitcoin')
  
  #Utlizamos a variavél 'moeda' para ver qual moeda o usuario deseja converter
  moeda = input('Escolha uma das moedas: ')
  valor = float(input('Escolha o valor que deseja converter: '))

  #com base na variavél 'moeda', alteramos seu valor para enviarmos uma requisição para a biblioteca AwesomeAPI
  if moeda == '1':
    moeda = 'USD'
    sigla = '$'
  elif moeda == '2':
    moeda = 'EUR'
    sigla = '€'
  elif moeda == '3':
    moeda = 'BTC'
    sigla = 'BTC'
  else:
    print('Moeda invalida.')

  #Buscando na biblioteca a cotação e fazendo a conversão
  conversao = float(data["{}BRL".format(moeda)]["bid"])
  print("Com R${} você pode comprar até {} {:.3f}".format(valor, sigla, valor/conversao))

elif cc == "2" or cc == "cotação das moedas":

  #Fazendo uma requisição a biblioteca e retornando a cotação de cada moeda
  print("Cotação das moedas:")
  print("Dólar: {}".format(data["USDBRL"]["bid"]))
  print("Euro: {}".format(data["EURBRL"]["bid"]))
  print("Bitcoin: {}".format(data["BTCBRL"]["bid"]))

else:
  print('Opção inválida.')
