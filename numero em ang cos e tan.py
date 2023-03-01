import random
y=input('Qual nome do primeiro aluno :')
x=input('Qual nome do segundo aluno :')
z=input('Qual nome do terceiro aluno :')
m=input('Qual nome do quarto aluno :')
lista=[y,x,z,m]
escolha=random.choice(lista)
print(escolha)