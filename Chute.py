
Digite = int(input('Chute um numero? '))
Acertou = False
while Acertou == False:
  if Digite == 2:
    Acertou == False
    print("Você acertou o numero é o numero 2")
    exit() # Se o usuario acertar ele acertou o código
  elif  Digite > 2:
   print('Você chutou um numero maior do que o numero correto') #caso não coloque o exit vai gerar um loop infinito e é essa intenção, será que estou criando uma criptografia?
  elif Digite < 2:
   print('Você chutou um numero menor do que o numero correto')
    #caso não coloque o exit vai gerar um loop infinito e é essa intenção, será que estou criando uma criptografia?

'''
import random
Digite = random.randint(1,10)
Acertou = False
while Acertou == False:
  Chute = int(input('Chute um numero de 1 a 10: '))
  if Chute == Digite:
    Acertou == True
    print("Você acertou o numero")
  elif Chute > Digite:
    print('Você chutou um numero maior do que o numero correto')
  elif Chute < Digite:
    print('Você chutou um numero menor do que o numero correto')
    '''