def verificar_nota(media):
    if media >= 7:
        print("Aprovado")
    elif media >= 5 and media < 7:
        print("Recuperação")
    else: 
        print("Reprovado")
media = float(input("Qual a média do aluno?: "))

verificar_nota(media)