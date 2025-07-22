from math import trunc

#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

num = float(input("Digite um numero real: "))
int = math.trunc(num)
print("A porção inteira do seu número real é {}".format(int))
