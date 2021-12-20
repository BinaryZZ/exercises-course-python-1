from datetime import date

ano = int (input('Digite um ano: '))
b = ano%4
ano_atual= date.today().year
print ('O ano {} é bissexto!'.format(ano) if b ==0 and ano % 100 != 0 or ano % 400 == 0
       else 'O ano {} não é bissexto!' .format(ano))

print ('Estamos no ano de {}' .format(ano_atual))
    #print('o ano {} é bissexto!'.format(ano) if bissexto == 0 else 'o       ano {} não é bissexto!'.format(ano))

