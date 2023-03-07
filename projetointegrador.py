print("="*30 + "ENTRADA DE DADOS" + "="*30 )



part_ina=float(input("Digite o quanto de MP10 existe no ar : "))
part_ina_fina=float(input("Digite o quanto de MP2.5 está no ar :"))
oz=float(input("Digite o quantidade de O3 que tem no ar :"))
dio_nitro=float(input("Digite a quantidade de N02 que possui no ar:"))
dio_enxo=float(input("Digite o valor da quantidade de SO2 que tem no ar:"))

#Aqui vai aparecer a qualidade boa  
print("="*30 + "Saída de Dados" + "="*30)
if part_ina >=0 and part_ina <=50:

     if part_ina_fina >=0 and part_ina_fina <=25:

        if oz >=0 and oz<=100:
            
             if dio_nitro >=0 and dio_nitro <=200:
                  
                  if dio_enxo >=0 and dio_enxo<=20:

                       print("A qualidade do ar está Boa, sem maiores problemas de saúde")

#Aqui vai aparecer a qualidade moderada
elif part_ina>50 and part_ina <=100:
     print("A qualidade do Ar está moderada")
elif part_ina_fina>25 and part_ina_fina <=50:
     print("A qualidade do Ar está moderada")
elif oz>100  and oz <=130:
     print("A qualidade do Ar está moderada")
elif dio_nitro>200 and dio_nitro <=230:
     print("A qualidade do Ar está moderada")
elif dio_enxo>20 and dio_enxo <=40:
     print("A qualidade do Ar está moderada")


#Aqui vai aparecer a qualidade ruim
elif part_ina>=100 and part_ina <=150:
     print("A qualidade do Ar está ruim")
elif part_ina_fina>=50 and part_ina_fina <=75:
     print("A qualidade do Ar está ruim")
elif oz >=130 and oz <=160:
     print("A qualidade do Ar está ruim")
elif dio_nitro>=230 and dio_nitro <=320:
     print("A qualidade do Ar está ruim")
elif dio_enxo >=40 and  dio_enxo<=365:
     print("A qualidade do Ar está ruim")

#aqui vai aparecer a qualidade muito ruim

elif part_ina >=150 and part_ina <=250:
     print("Qualidade do ar está muito ruim")
elif part_ina_fina >=75 and part_ina_fina <=125:
     print("Qualidade do ar está muito ruim")
elif oz >= 165 and oz <=200:
     print("Qualidade do ar está muito ruim")
elif dio_nitro >= 320 and dio_nitro <=1130:
     print("Qualidade do ar está muito ruim")
elif dio_enxo >= 365 and dio_enxo <=800:
     print("Qualidade do ar está muito ruim")


#aqui vai aparecer a qualidade péssima

elif part_ina >250:
     print("Qualidade do ar está péssima")
elif part_ina_fina>125:
     print("Qualidade do ar está péssima")
elif oz > 200:
     print("Qualidade do ar está péssima")
elif dio_nitro >1130:
     print("Qualidade do ar está péssima")
elif dio_enxo >800:
     print("Qualidade do ar está péssima")

    
        

