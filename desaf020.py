import random

n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o Segundo nome: '))
n3 = str(input('Digite o Terceiro nome: '))
n4 = str(input('Digite o Quarto nome: '))

s = random.sample([n1, n2, n3, n4], counts=None, k=4)
print ('A ordem de apresentação é {}' .format(s))