def verificar_atraso(dias):
    if dias > 0:
        print("\n\033[31mEmpréstimo bloqueado! Devolva o equipamento pendente.\033[m")
    elif dias == 0:
        print("\n\033[32mEmpréstimo liberado! Pode retirar novo equipamento.\033[m")
    else:
        print("\n\033[33mErro! Número incorreto.\033[m")