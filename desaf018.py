from math import cos, sin, tan, radians
v = int(input('digite o valor do ângulo: '))
acc = cos(radians(v))
abs = sin(radians(v))
t = tan(radians(v))
print ('O ângulo {} tem o arco cosseno de {:.4f}, o arco seno de {:.4f} \ne o arco cosseno de {:.4f} '
       .format(v,acc,abs,t))