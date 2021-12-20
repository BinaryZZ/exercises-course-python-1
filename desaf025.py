nome = input ('Digite seu nome: ')
nomel = nome.lower()
nome2 = nomel.find('silva')
if nome2 >= 0:
    print ('Este nome contém Silva!')

else:
        print ('Este nome não contem Silva!') #.format ('silva' in nome.lower())