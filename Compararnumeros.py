a = 11
b = 11
c = 3
  
  
if((a>b and a>c) and (a != b and a != c)): 
    print(a, " é o maior") 
elif((b>a and b>c) and (b != a and b != c)): 
    print(b, " é o maior") 
elif((c>a and c>b) and (c != a and c != b)): 
    print(c, " é o maior") 
else: 
    print("Os numeros são iguais") 