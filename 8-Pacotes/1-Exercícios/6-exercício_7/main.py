#Exercício 7: A Bilheteira do Cinema (Nível: Avançado)

#Objetivo: Utilizar um laço while para recolher múltiplos dados, enviá-los para um módulo externo e acumular os 
#resultados usando variáveis com nomes semânticos e claros.


#* Cria um ficheiro chamado cinema.py. Lá dentro, desenvolve uma função chamada calc_bilhete(idade).

#* A regra de negócio é: se a idade for menor do que 12 anos, a função devolve o valor 10. Caso contrário (12 anos ou mais), devolve 20.

#* Cria o ficheiro main.py e importa a função calc_bilhete.

#* No programa principal, cria uma variável total = 0 (para guardar o dinheiro do caixa).

#* Cria uma variável idade = -1 (apenas para permitir que o laço inicie).

#* Cria um laço while que continue a executar enquanto a idade for diferente de 0.

#* Dentro do laço, pede ao utilizador para digitar a idade. Se a idade introduzida for maior do que zero, chama a função, guarda o 
#retorno na variável preco e soma esse valor ao total.

#* Fora do laço, imprime o valor total que o grupo deve pagar.

from cinema import calc_bilhete
total = 0
idade = -1

while idade != 0:
   age = int(input("Digite sua idade: "))
   if age == 0:
      break
   else:
      preco = calc_bilhete(age) 
      total += preco



print("O valor é: ", total)