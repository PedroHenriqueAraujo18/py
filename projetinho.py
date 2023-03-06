import math pow

print('=====================================ENTRADA DE DADOS=====================================')
nome=input("Digite seu nome :")
nome.split()
print("Bem vindo {}!".format(nome))

idade=int(input("qual sua idade, {} :".format(nome)))
peso=float(input("Qual seu peso, {} :".format(nome)))
altura=float(input("Qual sua altura em metros {} :".format(nome)))

print("=====================================Calculadora de IMC=====================================")
print('IMC=(PESO/(ALTURA^ALTURA))')
imc=(peso/(math.pow(altura,2)))

print("{} de idade {}, seu imc é : {}".format(nome,idade,imc))

if imc <=18.5:
    print("{} você está abaixo do peso".format(nome))
elif imc >= 18.5 and imc <24.9:
    print("{} você está no peso normal".format(nome))
elif imc >=25 and imc <29.9:
    print("{} você está acima do peso".format(nome))
    
elif imc >=30 and imc <35:
    print("{} você está com obesidade grau I".format(nome))
elif imc >=35 and imc<39.9:
    print("{} você está com obesidade grau II".format(nome))
else:
    print("{} você está com obesidade grau III".format(nome))
print("=====================================Cortador de Strings=====================================")
n2=input("Quer fazer algo com seu nome? S/N")
if n2 == 'S':
    print("Seu nome é alfanúmerico?",nome.isalnum())
    print("Seu nome tirando o primeiro string e o quarto string : ",nome[1:4])
    print("Seu nome tirando o segundo string e o quarto string : ",nome[2:4])
    print("Seu nome tirando o terceiro string e o quarto string : ",nome[3:4])
    print("Seu nome tirando todas strings: ",nome[4:4])
else:
   print("Ok")
print("=====================================Calculadora=====================================")
y=input("Precisa de uma calculadora? S/N :")
y.split()
if y == "S" or y == "s":
    num_1=int(input("Digite um valor :"))
    num_2=int(input("Digite outro valor :"))


    op_2=["Multiplicação""Divisão" "Subtração" "Soma"]
    op_2.join(op_2)
    
for n in op_2:
    print(n)

    op_1=input("Digite M para calcular multiplicação,D para divisão,S para soma e Sb para subtração : ")

    if op_1 == "M"  or  op_1 == "m":
     m=num_1*num_2
     print("A Multiplicação é = {}".format(m))
    elif op_1=="D": 
        d=num_1/num_2
        d_2=num_1%num_2
        print("A divisão é:{}, e seu resto {}".format(d,d_2))
    elif op_1 == "S" or op_1=="s":
        s=num_1+num_2
        print("A soma é:{}".format(s))
    elif op_1 == "Sb" or  op_1 =="sb":
        sub=num_1-num_2
        print("A subtração é:{}".format(sub)) 
    else:
        print('Fim do programa')

