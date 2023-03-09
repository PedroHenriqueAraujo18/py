#1) Desenvolver o algoritmo e o diagrama de blocos para implementar o cálculo de conversão DÓLAR-REAL.
#cotação do dia 08/03/2023 as 8:32h manhã

print("="*30 + "ENTRADA DE DADOS" + "="*30)
print("CONVERSOR DE MOEDAS")
escolha=input("Real ou Dólar :")

print("="*30 + "PROCESSAMENTO DE DADOS" + "="*30)
if escolha == 'Real':

    real=float(input("Digite o valor de real para dólar :"))


    if real>0:
        dolar=real/5.19
        print("o Valor em dólar é: {:.2f} dólares".format(dolar))
    else:
        while real<=0:
         real=float(input("Valor inválido, Digite o valor de real para dólar :"))

elif escolha == 'Dólar':
    dólar=float(input("Digite o  valor de dólar para real :"))

    if dólar>0:
        r=dólar*5.19
        print("Seu valor em real é: {:.2f} reais".format(r))
    else:
        while dólar <=0:
            dólar=float(input("Valor inválido, Digite o  valor de dólar  para real :"))

print("="*30 + "SAÍDA DE DADOS" + "="*30)