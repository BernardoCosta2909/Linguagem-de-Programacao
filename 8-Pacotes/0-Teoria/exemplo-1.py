from colorama import Fore, Back, Style, init

init()

print(Fore.GREEN + "Olá turma! Este texto é verde")
print(Back.RED + Fore.WHITE + "Fundo vermelho e texto branco!")
print(Style.RESET_ALL + "Texto normal novamente")