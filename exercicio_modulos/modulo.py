import statistics as st

def moda(lista):
    print(f'Moda: {st.mode(lista):.1f}')

def media(lista):
    print(f'Média: {st.mean(lista):.1f}')

def desvio_padrao(lista):
    print(f'Desvio Padrão: {st.stdev(lista):.1f}')

def maior_nota(lista):
    print(f'Maior nota: {max(lista):.1f}')

def menor_nota(lista):
    print(f'Menor nota: {min(lista):.1f}')

def mediana(lista):
    print(f'Mediana: {st.median(lista):.1f}')


def analise_dados(lista):
    print(f'''
            
            +++++++++++++++++++++++++++
            Análise dos Salários
            +++++++++++++++++++++++++++
            ''')
    i = 0
    while i < len(lista):
        print(f'Nome da empresa: {lista[i]['nome']}')
        print(f'Salários: {lista[i]['salarios']}')
        media(lista[i]['salarios'])
        moda(lista[i]['salarios'])
        mediana(lista[i]['salarios'])
        desvio_padrao(lista[i]['salarios'])
        print('----------------------')
        i += 1