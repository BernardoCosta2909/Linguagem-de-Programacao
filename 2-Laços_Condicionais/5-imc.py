altura = float(input("\nInsira sua altura em metros: "))
peso = float(input("\nInsira seu peso em quilogramas: "))

imc = peso / (altura * altura)
print("\nSeu IMC é: ", imc)

if imc <= 18.5:
  print("\nVocê está abaixo do seu peso ideal.")

elif imc < 25:
 print("\nVocê está no seu peso ideal.")

elif imc < 30:
 print("\nVocê está dentro da faixa de sobrepeso.")

else:
   print("\nVocê está acima do peso.")