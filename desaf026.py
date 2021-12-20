frase = input('Digite uma frase: ')
frasel = frase.lower()
frase1 = frasel.count('a')
frase2 = frasel.find('a')+1
frase3 = frasel.rfind('a')+1
print ('Quantas vezes aparece a letra a:',frase1,'\n' 'A primeira letra a aparece na posição:'
       ,frase2,'\n''A letra a aparece pela última vez na posição:',frase3)