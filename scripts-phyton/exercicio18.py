import random

# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

#nomes = ["Ana", "Bruno", "João", "Bia"]
#nome_sorteado = random.choice(nomes)
#print(f"O aluno sorteado para apagar o quadro é {nome_sorteado}!")

n1 = str(input("Digite o nome do primeiro aluno: "))
n2 = str(input("Digite o nome do segundo aluno: "))
n3 = str(input("Digite o nome do terceiro aluno: "))
n4 = str(input("Digite o nome do quarto aluno: "))
lista = [n1,  n2, n3, n4]
escolhido = random.choice(lista)
print(f"O aluno escolhido foi {escolhido}! ")



