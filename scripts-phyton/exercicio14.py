# Aluguel de carros

km = float(input("Km percorridos: "))
dia = int(input("Dias  alugados: "))
preco_dia = dia  * 60
preco_km = km * 0.15
total = preco_dia + preco_km
print("O valor total a ser pago pelo aluguel do carro é R$ {:.2f} ".format(total))
