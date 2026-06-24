# ***EXERCÍCIOS com match/ case:*** 

# ***3: Verificando se uma string é vazia ou não***

texto = ''

match texto:
    case '':
        print('String vazia')
    case _:
        print('String não está vazia')

# ***5: Classificando uma idade em faixas etárias -  criança(12), adolescente(17), jovem(35), adulto 35 ><64, idoso(65)***

idade = 10

match idade:
    case idade if idade <= 12:
        print('Criança')
    case idade if 13 <= idade <= 17:
        print('Adolescente')
    case idade if 18 <= idade <= 35:
        print('Jovem')
    case idade if 36 <= idade <= 64:
        print('Adulto')
    case _:
        print('Idoso')