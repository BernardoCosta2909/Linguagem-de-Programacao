emprestimo = float(input("qual o valor desejado para empréstimo?: "))
idade = int(input("\nqual a sua idade?: "))
renda_mensal = float(input("\nqual sua renda mensal?: "))
parcela = float(input("\nquantas parcelas deseja?: "))

valor_parcela = emprestimo / parcela

if idade >= 21 and idade <= 65 and valor_parcela < (renda_mensal *0.30):
 print("\nvocê foi aprovado para o empréstimo.")
else:
 print("\nvocê não foi aprovado para o empréstimo.")
 
 
print("\nvalor do empréstimo é: ", emprestimo)
print("\nsua idade é: ", idade)
print("\nsua renda mensal é: ", renda_mensal)
print("\no número de parcelas desejadas são: ", parcela)
print("\no valor da sua parcela é de: ", valor_parcela)
print("\n30% da renda é igual a: ", renda_mensal *0.30)