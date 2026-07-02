from modulo_aula13 import num_pares, num_aleatorio, random_3, contagem_regressiva, tabuada, num_10_30

# 1 - Crie um número aleatório de 5,10
num_aleatorio()

# 2 - Crie 3 números aleatórios
random_3()

# 3 - Crie um número aleatório entre 10 a 30 utilize o range()
lista = list(range(10,31))
num_10_30(lista)

# 4 - Contagem regressiva simples
# Escreva um programa que exiba uma contagem regressiva de 10 a 1, e depois imprima "Fogo!". (loop for)
contagem_regressiva()

# 5 - Soma de números pares
# Peça ao usuário que insira um número inteiro positivo e, em seguida, calcule a soma de todos os números pares de 2 até o número inserido.
# # Peça ao usuário que insira um número inteiro faça o loop com range e for até o numero positivo
# # Em seguida, calcule a soma de todos os números pares de 2 até o número inserido. (use módulo, if, for)
n = int(input('Insira qualquer número positivo: '))
num_pares(n)

# 6 - Tabuada de multiplicação
# *Utilize print() na saída*
# Peça ao usuário para inserir um número inteiro e mostre a tabuada de multiplicação desse número de 1 a 10. (while ou for)
m = int(input('Qual tabuada você quer ver? '))
tabuada(m)