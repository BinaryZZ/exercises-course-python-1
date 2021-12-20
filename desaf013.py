s = float(input('Digite o seu salário atual: '))
va = 0.15
a = float(1+va)
sa = float(s*a)
print ('O seu salário de {:.2f} com o aumento de 15% passará a ser {:.2f}'
       .format(s,sa))