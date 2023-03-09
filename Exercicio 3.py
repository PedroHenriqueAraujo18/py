
print("="*30 + "ENTRADA DE DADOS" + "="*30)

print("CALCULADORA DE SEGUROS")


VBS=float(input("Digite o valor do bem a ser segurado :"))
USER=int(input("Digite quantos usúarios usaram : "))
TS=float(input("Qual é a taxa de seguro : "))
DS=float(input("Digite a taxa de desconto: "))
NP=int(input("Digite o número de parcelas: "))


if VBS  and TS and DS and NP >=0:

        print("="*30 + "PROCESSAMENTO DE DADOS" + "="*30)
 
        VSEG=VBS*TS/100

        VUSER = VSEG * USER / 100

        DESC = (VSEG + VUSER) * DS / 100

        SEG = VSEG + VUSER - DESC

        VPARCELA = SEG / NP

        print("O valor  do seguro bruto é {:.2f}, do adicional de usuário {:.2f}, do desconto é {:.2f}, do seguro liquido é {:.2f}, e das parcelas {:.2f}".format(VSEG,VUSER,DESC,SEG,VPARCELA))
else:
         while VBS  and TS and DS and NP <0:

            print("Valores inválidos, Digite Novamente.")
            BS=float(input("Digite o valor do bem a ser segurado :"))
            TS=float(input("Qual é a taxa de seguro : "))
            DS=float(input("Digite a taxa de desconto: "))
            NP=int(input("Digite o número de parcelas: "))

            while USER < 0:
                print("Número de Usuários inválidos, Digite novamente.")
                USER=int(input("Digite quantos usúarios usaram : "))

print("="*30 + "SAÍDA DE DADOS" + "="*30)