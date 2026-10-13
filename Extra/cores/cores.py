Cores_T = {
    
    "limpa":"\033[m",
    "Branco":"\033[:30m",
    "Vermelho":"\033[31m",
    "Verde":"\033[32m",
    "Amarelo":"\033[33m",
    "Azul":"\033[34m",
    "Violeta":"\033[35m",
    "Ciano":"\033[36m",
    "Cinza":"\033[37m",

    "petro&Branco":"\033[7:30m"
}

Cores_F = {
    
    "limpa":"\033[m",
    "Branco":"\033[7:40m",
    "Vermelho":"\033[41m",
    "Verde":"\033[42m",
    "Amarelo":"\033[43m",
    "Azul":"\033[44m",
    "Violeta":"\033[45m",
    "Ciano":"\033[46m",
    "Cinza":"\033[47m",
}


Titulo = "Inserindo Cores"
print('{}{:=^40}{}'.format(Cores_T["Ciano"],Titulo,Cores_T["limpa"]))

print("Letra Branca {}Fundo Branco{}".format(Cores_F["Branco"],Cores_F["limpa"]))
print("{}Letra Vermelha{} {}Fundo Vermelho{}".format(Cores_T["Vermelho"],Cores_T["limpa"],Cores_F["Vermelho"],Cores_F["limpa"]))
print("{}Letra Verde{} {}Fundo Verde{}".format(Cores_T["Verde"],Cores_T["limpa"],Cores_F["Verde"],Cores_F["limpa"]))
print("{}Letra Amarelo{} {}Fundo Amarelo{}".format(Cores_T["Amarelo"],Cores_T["limpa"],Cores_F["Amarelo"],Cores_F["limpa"]))
print("{}Letra Azul{} {}Fundo Azul{}".format(Cores_T["Azul"],Cores_T["limpa"],Cores_F["Azul"],Cores_F["limpa"]))
print("{}Letra Violeta{} {}Fundo Violeta{}".format(Cores_T["Violeta"],Cores_T["limpa"],Cores_F["Violeta"],Cores_F["limpa"]))
print("{}Letra Ciano{} {}Fundo Ciano{}".format(Cores_T["Ciano"],Cores_T["limpa"],Cores_F["Ciano"],Cores_F["limpa"]))
print("{}Letra Cinza{} {}Fundo Cinza{}".format(Cores_T["Cinza"],Cores_T["limpa"],Cores_F["Cinza"],Cores_F["limpa"]))