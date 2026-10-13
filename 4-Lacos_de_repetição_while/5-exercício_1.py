numeros = 1
soma = 0

while numeros != 0:
 numeros = int(input("\ndigite um número inteiro(se quiser parar a equação digite 0): "))
 soma += numeros 
 if numeros== 0: 
   break

print("\na soma dos números é: ", soma)