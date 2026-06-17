nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: ")) 
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3

aprovado = media >= 7
recuperacao = media >= 5 and media < 7
reprovado = media < 5

mensagem = (media >= 7) and "Aprovado" or (media >= 5 and media < 7) and "Recuperação" or "Reprovado" 

print(mensagem)