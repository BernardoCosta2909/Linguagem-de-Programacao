const guindaste = {
    operador: 'Carlos',
    cargaAcumulada: 0,
    limiteSeguranca: 50,
}

console.log('\nOperador:', guindaste.operador)

for (let i = 1; i <= 4; i++) {
    pesoContainer = 15 * i;
    guindaste.cargaAcumulada += pesoContainer;

    if(guindaste.cargaAcumulada >= guindaste.limiteSeguranca) {
        console.log('\nALERTA DE SOBRECARGA!!!')
        break
    } else {
        console.log('Quantidade do Contêiner:', pesoContainer)
        console.log('Carga acumulada:', guindaste.cargaAcumulada)
    }
}