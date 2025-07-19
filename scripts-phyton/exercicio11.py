#calculando desconto

preco = float(input("Qual o preço do produto?  R$ "))
desconto = preco - (preco * 5  / 100)
print("O preço do produto com desconto é {:.2f} reais".format(desconto))

