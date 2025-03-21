#Importando a biblioteca AwesomeAPI, para obter a cotação das moedas em tempo real
import requests

response = requests.get("https://economia.awesomeapi.com.br/last/USD,EUR,BTC")
data = response.json()

#Dando boas vinda e perguntando qual função o usuario deseja acessar
print('Olá, seja bem vindo ao meu conversor de moedas!!')
print('Primerio escolha uma das opções a seguir (colocar apenas o numero)')

cc = input("1. Conversor de moedas \n2. Cotação das moedas\n")

if cc == "1" or cc == "conversor de moedas":
  print('Escolha uma das moedas a seguir:')
  
  #Utlizamos a variavél 'moeda' para ver qual moeda o usuario deseja converter
  moeda = input('1. Dólar \n2. Euro \n3. Bitcoin\n')
  valor = float(input('Escolha o valor que deseja converter: '))

  #com base na variavél 'moeda', alteramos seu valor para enviarmos uma requisição para a biblioteca AwesomeAPI
  if moeda == '1':
    moeda = 'USD'
  elif moeda == '2':
    moeda = 'EUR'
  elif moeda == '3':
    moeda = 'BTC'

  #Buscando na biblioteca a cotação e fazendo a conversão
  conversao = float(data["{}BRL".format(moeda)]["bid"])
  print("Com R${} você pode comprar até {:.3f}".format(valor, valor/conversao))

elif cc == "2" or cc == "cotação das moedas":

  #Fazendo uma requisição a biblioteca e retornando a cotação de cada moeda
  print("Cotação das moedas:")
  print("Dólar: {}".format(data["USDBRL"]["bid"]))
  print("Euro: {}".format(data["EURBRL"]["bid"]))
  print("Bitcoin: {}".format(data["BTCBRL"]["bid"]))