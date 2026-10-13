numero_1 = float(input("digite um número: "))
operacao = str(input("\nescolha uma operação básica(+, -, * ou /): "))
numero_2 = float(input("\ndigite um número: "))

soma = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2

match operacao:
    case "+":
        print("\nresultado: ", soma)
    case "-":
        print("\nresultado: ", subtracao)
    case "*":
        print("\nresultado", multiplicacao)
    case "/":
        print("\nresultado", divisao)
    case _:
        print("\nVocê não sabe digitar!")