nome = str(input('Digite seu nome: '))
v = int(input('Digite o valor em metros para ser convertido em centímetros e milímetros: '))
c = v*100
m = v*1000
print ('Olá {} o valor {} em metros é o equivalente a {} centímetros ou {} milímetros!'
       .format(nome,v,c,m))