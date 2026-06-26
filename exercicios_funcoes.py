# ***1*** 
# ***CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.***

def comparar(n1,n2):
    if n1 % 2 == 0:
        print(f'{n1} é número par.')
    else:
        print(f'{n1} é número ímpar.')
    
    if n2 % 2 == 0:
        print(f'{n2} é número par.')
    else:
        print(f'{n2} é número ímpar.')

comparar(3,4)

# ***2***
# ***CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.***

def multi(n1,n2,n3):
    print(n1 * n2 * n3)

multi(4,5,6)

# ***3***
# ***CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.***

def raiz_quadrada(n):
    print(n ** 2)

raiz_quadrada(3)

# ***4***
# ***CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS.***

def mensagem_dezoito(idade,nome):
    if idade == 18:
        print(f'Seja bem vindo(a), {nome}!')
    else:
        print('Seja bem vindo(a)!')

mensagem_dezoito(18,'Ana')
mensagem_dezoito(20,'Carlos')

# ***5***
# ***DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.***

def descubra_idade(ano):
    print(f'Você tem {2026 - ano} anos')

descubra_idade(1995)
    
# ***6***
# ***DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.***

def brasil_ganhou(ano):
    vitorias = [1958, 1962, 1970, 1994, 2002]
    copas = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022, 2026]
    
    if ano in vitorias:
        print(f'O Brasil ganhou em {ano}')
    elif ano not in copas:
        print(f'Não teve Copa do Mundo em {ano}')
    else:
        print(f'O Brasil não ganhou em {ano}')

brasil_ganhou(1999)

# ***7*** 
# ***DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.***

def pedido_restaurante():
    pedido = []

    salada = input(f'Gostaria de salada? s/n: ')
    macarronada = input(f'Gostaria de macarronada? s/n: ')
    sanduiche = input(f'Gostaria de sanduiche? s/n: ')
    sorvete = input(f'Gostaria de sorvete? s/n: ')

    if salada == 's' or salada == 'S':
        pedido.append('Salada')
    if macarronada == 's' or macarronada == 'S':
        pedido.append('Macarronada')
    if sanduiche == 's' or sanduiche == 'S':
        pedido.append('Sanduíche')
    if sorvete == 's' or sorvete == 'S':
        pedido.append('Sorvete')
    
    print(f'Seu pedido é: {pedido}')

pedido_restaurante()