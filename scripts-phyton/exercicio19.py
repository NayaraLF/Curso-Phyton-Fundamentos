import random
from random import shuffle

#O mesmo professor do desafio 18 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

n1 = str(input("Digite o nome do primeiro aluno: "))
n2 = str(input("Digite o nome do segundo aluno: "))
n3 = str(input("Digite o nome do terceiro aluno: "))
n4 = str(input("Digite o nome do quarto aluno: "))
lista = [n1,  n2, n3, n4]
#sorteados = random.sample(lista, 4)
#print(f"A sequencia de alunos sorteados foi {sorteados}!")

shuffle(lista)
print("A ordem de apresentação será ")
print(lista)
