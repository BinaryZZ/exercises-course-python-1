s = float(input('Digite o valor do salário: '))
a1 = 1.10
a2 = 1.15
a3 = 0.10
a4 = 0.15

print ('O seu novo salário será de R${:.2f} reais com aumento de R${} reais'.format(s*a1,s*a3) if s >=1250
       else 'O seu novo salário será de R${:.2f} reais com aumento de R${} reais' .format(s*a2,s*a4))