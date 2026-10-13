numero_1 = float(input("digite o primeiro número: "))
numero_2 = float(input("\ndigite o segundo número: "))
operacao = str(input("\nescolha uma operação básica(+, -, * ou /): "))

match operacao:
    case "+":
        print("\nresultado: ", numero_1 + numero_2)
    case "-":
        print("\nresultado: ", numero_1 - numero_2)
    case "*":
        print("\nresultado: ", numero_1 * numero_2)
    case "/":
        print("\nresultado: ", numero_1 / numero_2)
    case _:
        print("\nVocê não sabe digitar!")