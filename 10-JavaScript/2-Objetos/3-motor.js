const motor = {
    modelo: 'Yamaha V6',
    tempAtual: 50,
    tempMaxima: 85,
}

console.log('\nModelo do motor:', motor.modelo)
console.log('\nLimite de segurança:', motor.tempMaxima)

for (let i = 1; i <= 5; i++) {
    motor.tempAtual += 10;

    if (motor.tempAtual > motor.tempMaxima) {
        console.log('\nALERTA CRÍTICO!!!')
        break
    } else {
        console.log('\nFuncionamento normal!')
    }
}