#crie um programa que pede para o usuario 
#digitar 3 notas de um aluno. Em seguida o programa
#deve calcular a media e mostrar na tela

while True:
 nota_1 = float(input("digite o valor da nota: "))
 nota_2 = float(input("\ndigite o valor da nota: "))
 nota_3 = float(input("\ndigite o valor da nota: "))

 media = (nota_1 + nota_2 + nota_3) / 3
 
 print("\na media do aluno é: ", media)

 if media >= 6:
    print("\nO aluno foi APROVADO")

 else:
   print("\nO aluno foi REPROVADO")

 if media >= 8: print("\nO aluno foi um ALUNO DESTAQUE")

 if media < 5: print("\nO aluno precisa de REFORÇO")

 if media <= 0: print("\nNão sobrou nada pra esse Beta")

 if media >= 10: print("\nEsse é o Alfa Sigma do 67")

 saida = str(input("\nse deseja sair digite 'sair', se não aperte a tecla enter: "))
 if saida == "sair": break

 
 

 