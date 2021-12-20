distancia = int (input('Quantos kilômetros serão de viagem? '))
distancia1 = distancia*0.50
distancia2 = distancia*0.45
#preço = distancia * 0.50 if distancia <=200 else distancia * 0.45
print ('O valor da viagem será de R${:.2f} reais para percorrer {} Kilômetros' .format(distancia1,distancia) if distancia <= 200
       else 'O valor da viagem será de R${:.2f} reais para percorrer {} Kilômetros'.format(distancia2,distancia) )