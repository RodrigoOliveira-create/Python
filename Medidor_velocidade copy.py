Velocidade = int(input('Qual foi a velocidade do veiculo? '))
Velocidade_Maxima = 80
if Velocidade <= Velocidade_Maxima:
  print('Não tem multa')
elif Velocidade > Velocidade_Maxima and Velocidade <= Velocidade_Maxima + 10:
    print('Levou Multa leve ')
elif Velocidade > Velocidade_Maxima + 11 and Velocidade <= Velocidade_Maxima + 20:
   print('Levou Multa Grave ')
elif Velocidade > Velocidade_Maxima + 20:
    print('Levou Multa Gravissima ')
  #Tem que se atentar aos espaçamentos "elif, if"