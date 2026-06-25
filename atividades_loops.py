# Atividade 1 ----------------------------------
# 1

n = 0
while n <= 1000:
    print(n, end=', ')
    n += 1

# 2

l = []
num = 1
while num <= 10:
    nomes = input('Digite um nome: ')
    l.append(nomes)
    num += 1
print(l)

# Atividade 2 ----------------------------------

# **Sistema de notas de alunos**
# - Acesso a conta com condicionais
# - 3 chances de acessar o sistema
# - Após errar 3 x mensagem que diga que a conta bloqueada (senha incorreta)
# - Inserir notas (se Senha correta)
# - Fazer a média
# - Utilize ***loops for, while, condicionais, variáveis, listas, tuplas ou dicionários…***

# ***IMPORTANTE:***
# - Ao finalizar o código, insira na borda do script, no última linha:
# input(’Digite enter para sair’)

print(f'''
      *****************************************************
      SISTEMA DE NOTAS
      *****************************************************
      ''')

for i in range(3):
    senha = int(input('Digite sua senha: '))
    alunos = []
    if senha == 123:
        while True:
            print(f'''
                    Bem vindo ao sistema de notas!
                    ''')
            x = int(input('Quantos médias de alunos você quer registrar? '))
            cont = 0
            
            while cont < x:
                nome = input('Digite o nome do aluno: ')
                nota1 = float(input('Digite a 1a nota: '))
                nota2 = float(input('Digite a 2a nota: '))
                nota3 = float(input('Digite a 3a nota: '))
                media = (nota1 + nota2 + nota3) / 3
                print(f'A média final do aluno {nome} é {media}')
                alunos.append({nome: media})
                cont += 1
            
            print(f'Lista de médias dos alunos:\n{alunos}')

else:
    print('Conta bloqueada!')
    input('Digite enter para sair')

