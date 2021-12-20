import random
#Import da função random para uso no programa

#estrutura de repetição para manter o usuario em loop até digitar a opção para encerrar o programa
while True:
 print('Bem-vindo ao nosso curso!')
 print('Aviso: É necessário sua inscrição para o recebimento do voucher! ')
 print('Digite 1 para efetuar sua inscrição.')
 print('Digite 2 para visualizar sua inscrição.')
 print('digite 3 para encerrar.')
 numero=random.randint(100,400)
 try:
  perg = int(input('O que deseja fazer? '))
 except:
#como perg e uma variavel do tipo inteiro, uso do try/except para casos onde o usuario digite caracteres
   print('Opção invalida,por favor digite uma das 3 dispostas...')
   continue
#condicionais para responderem ao dado inputado na variavel perg
 if perg==1:
      nome=input('Por favor digite o seu nome: ')
      email=input('Por favor digite o seu email: ')
      telefone=input('Agora o seu telefone: ')
      curso=input('Digite o seu curso: ')
      lista1 = [{'Voucher': numero, 'Nome: ': nome, 'Email: ': email, 'Telefone: ': telefone, 'Curso: ': curso}]
      print('Dados salvos com sucesso..')
#print da inscrição inputada na condicional ==1
 elif perg==2:
    try:
     print(lista1)
    except:
#mais um try/except para o usuario que digitar para ver sua inscrição antes de inputar os dados
        print('Nenhuma inscrição cadastrada...')
        continue
#condicional para termino do programa para o fim da estrutura de repetição
 elif perg==3:
   print('Encerrando o programa...')
   break
#else para qualquer valor atribuido a variavel perg que seja inteiro e não seja 1,2 ou 3
 else:
     print('Opção invalida')





