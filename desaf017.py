import math

co = int(input('Digite o comprimento do cateto oposto: '))
ca = int(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = ((ca**2)+(co**2))
print ('A hipotenusa de um triângulo com o cateto oposto de {}cm e cateto adjacente de {}cm'
       '\né = {} '.format(co,ca,math.sqrt(hipotenusa)))