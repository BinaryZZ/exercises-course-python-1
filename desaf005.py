nome = str(input('Digite seu nome: '))
num = int(input('Digite o valor: '))
s = (num+1)
a = (num-1)
print('Olá {}!, o sucessor de {} é {} e o antecessor de {} é {}'
      .format(nome,num,s,num,a))