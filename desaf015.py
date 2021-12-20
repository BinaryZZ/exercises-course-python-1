d = int(input('Qual a quantidade de dias de uso: '))
k = float(input('Quantos kilômetros foram rodados? '))
vd = float(60)
vk = float(0.15)
vfd = d*vd
vfk = k*vk
vap = vfd+vfk
print ('Você alocou o carro por {} dias e rodou {:.2f} kilômetros\nportanto o valor a pagar é de R${:.2f} reais'
       .format(d,k,vap))