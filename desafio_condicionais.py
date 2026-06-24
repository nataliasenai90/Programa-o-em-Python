clientes = []

cadastro = {
    "nome": input("Digite seu nome:"),
    "idade": input("Digite sua idade:")
}

print(cadastro)

print(f'''
      Bem vindo, {cadastro["nome"]}!

      Gostaria de fazer uma reserva?
      ''')

reserva = input("Digite Sim ou Não: ")

if reserva == "Sim" or reserva == "sim":
    quarto = int(input(f'''Escolha o tipo de quarto:
                   
                   1. Simples
                   2. Duplo
                   3. Luxo
                       
                   (digite o número):
                
                   '''))
    
    if quarto == 1:
        preco = 100.0
    elif quarto == 2:
        preco = 150.0
    elif quarto == 3:
        preco = 250.0
    else:
        print('Erro!')

    dias = int(input(f'Por quantos dias você ficará hospedado? (digite a quantidade de dias): '))

    estadia = preco * dias

    pagamento = int(input(f'''O valor da sua estadia será de R$ {estadia}.
                          
                          Qual será a forma de pagamento?
                          
                          1. Débito
                          2. Crédito
                          3. Pix
                          
                           (digite o número): 
                          '''))
    
    if pagamento == 1:
        print('A forma de pagamento escolhida foi débito. Obrigado por escolher o nosso hotel!')
    elif pagamento == 2:
        print('A forma de pagamento escolhida foi crédito. Obrigado por escolher o nosso hotel!')
    elif pagamento == 3:
        print('A forma de pagamento escolhida foi Pix. Obrigado por escolher o nosso hotel!')
    else:
        print('Erro! Valor inválido!')
else:
    print('Fim!')