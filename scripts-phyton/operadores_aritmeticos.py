#Operadores aritmeticos

# 5 +3 == 8
#Ordem de precedencia em phyton
# 1:  ()
#2:   **    exponenciação
#3:  *, /, //, %
#4: +, -

n1 = int(input("Um valor"))
n2 = int(input("Outro valor"))
soma = n1+n2
multiplica = n1*n2
divisao = n1/n2
divisaointeira = n1 // n2
exponenciacao = n1 **n2

print("A soma vale {}, o produto é {}, e a divisao é {} {:.3f}".format(soma, multiplica, divisao))
print("Divisao inteira {} e potencia {}".format(divisao, exponenciacao))
