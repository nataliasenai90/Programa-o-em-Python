# Exercícios sobre listas (Aula 7)

# 0
num_pares = list(range(2,21,2))
print('0: ', num_pares)

# 1
numeros = list(range(1,11))
print('1: ', numeros)

# 2
print('2: ', numeros[2])

# 3
numeros.append(9)
print('3: ', numeros)

# 4
del numeros[4]
print('4: ', numeros)

# 5
carros = ['Volkswagen', 'Toyota', 'Renault']
carros += numeros

print('5: ', carros)
