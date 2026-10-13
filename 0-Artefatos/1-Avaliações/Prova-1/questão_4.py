valor_do_produto = float(input("qual o valor do produto?: "))
forma_de_pagamento = input("\nse o pagamento for à vista, digite '1', se for parcelado, digite '2': ")

parcelado = valor_do_produto / 3

a_vista = valor_do_produto * 0.90

if forma_de_pagamento == "1":
 print("\nà vista, valor: ", a_vista )
else:
   print("\nParcelado, valor à pagar: ", parcelado)



