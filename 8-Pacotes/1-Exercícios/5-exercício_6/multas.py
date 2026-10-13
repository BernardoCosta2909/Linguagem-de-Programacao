def calcular_infracao(limite_via, velocidade_carro):

    if velocidade_carro <= limite_via and velocidade_carro > 0: 
        return "\n\033[32mBoa viagem! Dentro do limite.\033[m"
    elif velocidade_carro >= limite_via and velocidade_carro <= limite_via + 20: 
        return "\n\033[33mInfração Média! Multa de R$ 130,16.\033[m"
    elif velocidade_carro > limite_via + 20:
        return "\n\033[31mInfração Gravíssima! Multa de R$ 880,41 e suspensão da CNH.\033[m"
    else: 
        return "\n\033[7:30mVelocidade indisponível!\033[m"
