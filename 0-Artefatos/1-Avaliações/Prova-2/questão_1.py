carga = int(input("Classifique o tipo de carga (1, 2, 3, 4 ou 5): "))

match carga:
    case 1 | 2 | 3:
        print("\nCarga geral / Manufaturados.")
    case 4 | 5:
        print("\nProdutos perecíveis / Refrigerados.")
    case _:
        print("\nCódigo inválido - Consultar o surpevisor.")