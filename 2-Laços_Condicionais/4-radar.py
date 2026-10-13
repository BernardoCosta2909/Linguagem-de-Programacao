velocidade = int(input("\nQual a velocidade do veículo: "))

if velocidade <= 80: 
 print("\nParabéns, você é um ótimo condutor. ")
else: 
 print("\nvocê foi um péssimo condutor e pagará uma multa.")

 multa = (velocidade - 80) * 7 

 print("\nO valor da sua multa é: ", multa )