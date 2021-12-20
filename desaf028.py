from random import randint
pc = randint(0,5)
pl = int (input ('Tente adivinhar o número de 0 a 5: '))
if pl == pc:
    print ('Eu pensei no número {}\nParabéns! você venceu :)) ' .format(pc))
else:
    print ('Eu pensei no número {}\nVocê perdeu! mais sorte na próxima' .format(pc))