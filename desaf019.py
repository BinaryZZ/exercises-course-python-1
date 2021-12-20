from random import sample

n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o Segundo nome: '))
n3 = str(input('Digite o Terceiro nome: '))
n4 = str(input('Digite o Quarto nome: '))

s = sample([n1, n2, n3, n4], counts=None, k=1)
print ('O vencedor do sorteio é {}' .format(s))