num = input('Digite um número:')
erro: str = 'Por favor, digite um valor de 0 a 9999'

#unidade = num // 1 % 10
#dezena = num // 10 % 10
#centena = num // 100 % 10
#milhar = num // 1000 % 10

if len (num) <= 1:
    print('unidade:',num)

if len (num) == 2:
    print('dezena:',num[0],'unidade:',num[1])

if len (num) == 3:
    print('centena:',num[0],'dezena:',num[1],'unidade:',num[2])

if len (num) == 4:
    print('milhar:',num[0],'centena:',num[1],'dezena:',num[2],'unidade:',num[3])

if len (num) >= 5:
    print (erro)
