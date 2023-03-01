car=float(input("Informe a a quantidade de km percorridos:"))
d=int(input("Informe quantos por quantos dias foi alugado:"))
d=d*60
car=car*0.15
price=d+car

print("-"*20)
print("O preço a pagar somando o km rodado e o aluguel é{}".format(price))
print("-"*20)