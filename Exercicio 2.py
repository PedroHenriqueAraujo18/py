print("="*30 + "ENTRADA DE DADOS" + "="*30)

nome=input("Digite seu nome:")
print("Bem vindo {}".format(nome))
sb=float(input("Digite seu sálario bruto :"))
imp=0.1




if nome.lower():


  if sb >0:

     sl=sb-(sb*imp)
     print("{} O seu salário liquido é {}".format(nome,sl))

  else:
     while sb<0:
       print("Somente digite valores acima de 0 ")
       sb=float(input("Digite seu sálario bruto :"))

