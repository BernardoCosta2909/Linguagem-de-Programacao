import math

recursos = dir(math)

print(recursos)

numero = int(input("\nDigite um número para ser o número base: "))

potencia = int(input("\nDigite um número para ser a potência do cálculo: "))

print("\nO resultado da potenciação é:", math.pow(numero , potencia))