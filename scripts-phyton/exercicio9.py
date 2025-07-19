real = float(input("Qual valor você possui em reais?  R$"))
print("Esse valor convertido em dolar é {:.2f}".format(real/5.58))


#outra forma de resolver
real = float(input("Quanto dinheiro você tem em reais?  R$"))
dolar = real / 5.58
print("Com R${:.2f} você pode comprar U${:.2f}".format(real, dolar))
