idade = int(input("Digite sua idade: "))

if idade <= 12:
    print("Escalão Infantil")

elif idade >= 12 and idade < 18:
    print("Escalão Juvenil")
    
else:
    print("Escalão Aduto")

