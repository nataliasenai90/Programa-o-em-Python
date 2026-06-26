# Exercício 1:
# Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

try:
    num = int(input('Digite um número: '))
except ValueError:
    print('O valor digitado não é um número inteiro.')
except:
    print('O valor digitado não é um número.')
else:
    print(f'Você digitou: {num}')


# Exercício 2:
# Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.

try:
    div1 = int(input('Digite o dividendo: '))
    div2 = int(input('Digite o divisor: '))

    q = div1 / div2

except ZeroDivisionError:
    print('Não pode dividir por 0.')
except ValueError:
    print('Pelo menos um dos valores não é um número.')
except:
    print('Erro desconhecido.')
else:
    print(f'''Resultados da divisão: 
          - Dividendo: {div1}
          - Divisor: {div2}
          - Quociente: {div1/div2}
          - Divisão inteira: {div1//div2}
          - Resto: {div1%div2}''')


# Exercício 3:
# Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).

lista = [1,2,3,4,5]

try:
    i = int(input('Digite um número entre 0 e 4: '))
    print(lista[i])
except:
    print('erro')
