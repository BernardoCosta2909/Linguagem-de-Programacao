def converter_dolar(valor_dolar, cotacao):
    return valor_dolar * cotacao

valor1 = float(input("Digite o seu saldo em dólar: "))
valor2 = float(input("Digite a cotação do dólar hoje: "))

print("O valor em reais é: ", converter_dolar(valor1, valor2))