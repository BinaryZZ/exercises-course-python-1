nome = input('Digite o nome de uma cidade: ')
nomel = nome.lower()
nome2 = nomel.find('santo')
nome3 = nome.isnumeric()

if nome2 == -1:
    print('O nome desta cidade não começa com SANTO!')

if nome2 == 0:
    print ('O nome desta cidade começa com SANTO!')

if nome == 'True':
    print ('Por favor digite o nome de uma cidade!')