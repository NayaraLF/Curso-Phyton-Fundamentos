import math

# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

cat_o = float(input("Digite o comprimento do cateto oposto: "))
cat_a = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = math.hypot(cat_o, cat_a)
print(f"Os valores dos catetos são {cat_o} e {cat_a}, e o valor da hipotenusa é {hipotenusa}")
