import random
Digite = random.randint(1,10)
Acertou = False
while Acertou == False:
  Chute = int(input('Chute um numero de 1 a 10: '))
  if Chute == Digite:
    Acertou == True
    print("Você acertou o numero")
    exit() #Comando para sair do código após acertar
  elif Chute > Digite:
    print('Você chutou um numero maior do que o numero correto')
  elif Chute < Digite:
    print('Você chutou um numero menor do que o numero correto')
