import statistics as st

lista = [1,2,2,15,4,20,12,8,7,30,74,16,12,32,45,90,12,60]

media = st.mean(lista)
print(f'Média: {media}')

# desvio padrao
desvio = st.stdev(lista)
print(f'Desvio Padrão: {desvio}')

# variancia
variancia = st.variance(lista)
print(f'Variância: {variancia}')

# amplitude
amplitude = max(lista) - min(lista)
print(f'Amplitude: {amplitude}')

# moda
moda = st.mode(lista)
print(f'Moda: {moda}')

# mediana
mediana = st.median(lista)
print(f'Mediana: {mediana}')