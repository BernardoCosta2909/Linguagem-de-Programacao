idade = int(input("qual a sua idade: "))

tem_licenca = str(input("você tem licença? Digite sim ou não: "))

if tem_licenca == "sim" and idade >=18:
    print("você pode dirigir")

else: print("você não pode dirigir")
