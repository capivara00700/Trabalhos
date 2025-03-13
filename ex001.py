print('Olá, seja bem vindo ao meu conversor de moedas!!')
valor = float(input('Primeiro escolha um valor em R$ que você deseja converter: '))
escolha = str(input('Você deseja converter para Dólar ou Euro?: '))

if escolha.lower() == 'dolar' or escolha.lower() == 'dólar':
    print('com R${:.2f}, você pode comprar até ${:.2f} dólares.'.format(valor, valor/5.81))
elif escolha.lower() == 'euro':
    print('com R${:.2f}, você pode comprar até €{:.2f} euros.'.format(valor, valor/6.3092))
else:
    print('Desculpe mas não conheço está moeda.')

