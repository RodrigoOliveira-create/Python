Numero = int(input("Insira um numero para calculo fatorial ")) # VARIAVEL É O NUMERO, INT TRANSFORMA A INFORMAÇÃO QUE ESTÁ EM STRING PARA INTEIRO, INPUT PERMITE QUE O USUARIO INSIRA O NUMERO
if Numero > 0: # si o numero for igual a 0
  Fatorial = 1 # caso a resposta acima seja verdadeira a varialvel fatorial vai ser 1
for item in range(1,Numero +1):# multiplicação até o valor do numero digitado, é colocado +1 pois essa leitura sempre finaliza com um numero a menos, exemplo se o numero for 10 ele vai contar até o 9
  Fatorial = Fatorial * item # o fatorial é a multiplicação de cada numero acrescentado no for
print(Fatorial) # comando para mostrar o fatorial
