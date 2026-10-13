idade = int(input("Digite sua idade: "))

if idade <= 12:
    print("\nInfantil")

elif idade >= 12 and idade < 18:
    print("\nJuvenil")

else:
    print("\nAdulto")

seguro_saude = input("\nvocê tem seguro saúde? Digite 'sim' ou 'não': ")

if seguro_saude == "não" and idade >= 18:
    print("\nAtenção: Seguro saúde obrigatório para adultos.")

else:
    print("\nInscrição aceita.")
