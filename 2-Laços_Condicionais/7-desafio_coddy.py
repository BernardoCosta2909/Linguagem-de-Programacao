idade = int(input("qual a sua idade: "))

tem_licenca = input("você tem licença? Digite sim ou não: ")

if tem_licenca == "sim":
 tem_licenca = True
else:
   False

resultado = idade >= 18 and tem_licenca


print("pode dirigir?: ", resultado)

print(type(tem_licenca))
print(type(idade))