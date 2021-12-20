nome = input('Digite seu nome: ')
nome2 = nome.split()
nomelen= len(nome2)
nome3 = nomelen - 1
nome4 = nome.isnumeric()
if nome3 == 0:
    print ('O único nome inserido foi:',nome)


else:
    print ('O primeiro nome é:',nome2[0],'\n''O segundo nome é:',nome2[nome3])
