a = float(input('Digite a altura da parede em metros: '))
l = float(input('Digite a largura da parede em metros: '))
s = (a*l)
t = float(2.0)
rf = float(s/t)
print ('Para pintar uma área de {:.2f}m² você irá precisar de {:.2f} litros de tinta'
       .format(s,rf))