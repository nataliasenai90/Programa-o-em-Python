from modulo import media, moda, desvio_padrao, menor_nota, maior_nota

# Desafio 1

# notas_turma = [6.0, 7.5, 8.5, 10.0, 9.5, 5.0, 6.5, 7.5, 1.5, 4.0, 5.5, 7.0, 3.5]

# media(notas_turma)
# moda(notas_turma)
# desvio_padrao(notas_turma)
# menor_nota(notas_turma)
# maior_nota(notas_turma)

# Desafio 2

from modulo import analise_dados

empresas = [
   {'nome': 'empresa 1', 'salarios': [1000,6000,1200,8000,1400]},
   {'nome': 'empresa 2', 'salarios': [5000,4000,3000,2000,7000]},
   {'nome': 'empresa 3', 'salarios': [1200,1300,8000,3000,15000]},
   {'nome': 'empresa 4', 'salarios': [1400,1750,2000,4500,5900]} 
]

analise_dados(empresas)