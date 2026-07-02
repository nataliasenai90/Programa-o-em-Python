import random
import time

def num_pares(n):
    lista_num = []

    for x in range(2,n+1,2):
        lista_num.append(x)

    soma = sum(lista_num)
    print(f'Números: {lista_num} | Soma dos números: {soma}')

def num_aleatorio():
    print(random.randint(5,10))

def num_10_30(lista):
    print(random.randint(lista[0],lista[len(lista)-1]))

def random_3():
    print(random.randint(0,100), random.randint(0,100), random.randint(0,100))

def contagem_regressiva():
#     cont = 10
#     while cont <= 10:
#         if 0 < cont <=10:
#             print(f'{cont}')
#             time.sleep(1)
#             cont -= 1
#         else:
#             print(f'Fogo!')
#             break

    for x in range(10,-1,-1):
        if 0 < x <=10:
            print(f'{x}')
            time.sleep(0.5)
            x -= 1
        else:
            print(f'Fogo!')
            break

def tabuada(m):
    i = 1

    tabuada_m = []
    while i <= 10:
        tabuada_m.append(m * i)
        i += 1

    j = 1
    print(f'Tabuada de {m}:')
    while j <= 10:
        for x in tabuada_m:
            print(f'{m} x {j} = {x}')
            j += 1