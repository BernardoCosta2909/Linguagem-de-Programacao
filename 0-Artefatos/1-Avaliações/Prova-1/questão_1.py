# erro 1. falta um tipo na entrada de dados (float ou int)
# erro 2. falta ':' no if
# erro 3. falta ':' no else

# versão errada:
velocidade = input("Velocidade: ")
limite = 80

if velocidade > limite                                              #type:ignore
 print("você foi multado!")
else                                                                #type:ignore
   print("Velocidade OK.")

#versão correta:
velocidade = float(input("Velocidade: "))
limite = 80

if velocidade > limite: 
    print("\nvocê foi multado!")
else: 
    print("\nvelocidade ok.")