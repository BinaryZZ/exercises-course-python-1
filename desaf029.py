velocidade = int (input ('Qual a velocidade do carro em Km/h? '))
multa = velocidade - 80
print ('Você não foi multado' if velocidade <= 80 else 'Você foi multado em R${} Reais por estar ' \
       'acima do limite de velocidade permitido!' .format(multa*7))