nome = str(input('Digite seu nome: '))
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1+n2)/2
print ('Olá {}!\nSua primeira nota é {} e a segunda é {}\nportanto sua média é {}'
       .format(nome,n1,n2,m))