tempo = int(input("como está o dia hoje? (1 = ensolarado, 2 = chuvoso, 3 = nublado ou 4 = nevoso): "))

match tempo:
    case 1 | 3:
        print("\npasse protetor solar!!")
    case 2 | 4:
        print("\nuse um agasalho!!")
    case _:
        print("\nnúmero inválido")