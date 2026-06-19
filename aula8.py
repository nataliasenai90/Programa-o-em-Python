# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.

numero = int(input('Digite um número: '))

if numero == 0:
    print('Zero')
elif numero > 0:
    print('Positivo')
else:
    print('Negativo')

# -------------------------------------------------------------------------

# 2*
# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.

idade = int(input('Digite sua idade: '))

if idade > 15:
    print('Você pode votar!')

# -------------------------------------------------------------------------

# 3*
# Declara uma variável com um número qualquer, 
# determine se um número é par ou ímpar.

var = 457

if var % 2 == 0:
    print('Número par')
else:
    print('Número ímpar')

# -------------------------------------------------------------------------

# 4*
# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno

# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.

l1 = int(input('Digite o tamanho do lado 1: '))
l2 = int(input('Digite o tamanho do lado 2: '))
l3 = int(input('Digite o tamanho do lado 3: '))

if l1 == l2 == l3:
    print('Triângulo equilátero')
elif l1 != l2 and l2 != l3 and l1 != l3:
    print('Triângulo escaleno')
else:
    print('Triângulo isósceles')

# -------------------------------------------------------------------------

# 5*
# Determine se um número é múltiplo de 5 e 7.

num = int(input('Digite um número: '))

if num % 5 == 0 and num % 7 == 0:
    print('Este número é múltiplo de 5 e de 7!')
elif num % 5 == 0 and num % 7 != 0:
    print('Este número é múltiplo de 5!')
elif num % 5 != 0 and num % 7 == 0:
    print('Este número é múltiplo de 7!')
else:
    print('Este número não é multiplo de 5 e nem de 7!')

# -------------------------------------------------------------------------

# 6*
# Verifique se um número é positivo e maior que 10

n = int(input('Digite um número: '))

if n > 10:
    print('O número é positivo e maior do que 10.')
elif n > 0:
    print('O número é positivo, mas é menor do que 10.')
elif n == 0:
    print('O número é igual a zero.')
else:
    print('O número é negativo.')

# -------------------------------------------------------------------------

# 7*
# Verifique se um número é divisível por 3 ou 5.

number = int(input('Digite um número: '))

if number % 3 == 0 and number % 5 == 0:
    print('O número é divisível por 3 e por 5')
elif number % 3 == 0:
    print('O número é divisível por 3')
elif number % 5 == 0:
    print('O número é divisível por 5')
else: 
    print('O número não é divisível por 3 e nem por 5')