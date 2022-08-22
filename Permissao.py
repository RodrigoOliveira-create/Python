Permissao = ('Gerente') #A ideia é criar uma condição, tipo você está livre para sair


if Permissao == 'Diretor':
  print('usuário diretor')
elif Permissao == 'Gerente':
  print('É um Gerente')
elif Permissao == 'Usuario':
  print ('É um usuário')
else:
  print('Usuario não validado')