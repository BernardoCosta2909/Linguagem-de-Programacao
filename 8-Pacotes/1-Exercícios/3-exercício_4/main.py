from seguranca import validar_login

name = input("Qual o nome do usuário?: ")
password = input("Qual é a senha?: ")

validar_login(name, password)