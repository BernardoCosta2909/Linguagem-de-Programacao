temperaturas = [22, 15, 14, 25, 17, 28, 13]

contador = 0

dias = 0

media = 0

for b in temperaturas:
 print("\ntemperatura do dia: ", b, "°C")
 media += b
 dias += 1
 if b <= 18:
    contador += 1

print("\nA temperatura ficou abaixo de 18° durante", contador, "dias")

print("\nA média das temperaturas é:{:.2f} ".format(media / dias))