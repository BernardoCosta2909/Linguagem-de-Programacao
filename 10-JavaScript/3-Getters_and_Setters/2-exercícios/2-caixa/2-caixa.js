console.log("--- Caixa ---")

const conta = {

    _nome: "Bernardo",
    _saldo: 500,

    get saldo() {
        return this._saldo + "R$ disponíveis."
    },

    set saldo(novoSaldo) {
        if (novoSaldo <= -501) {
            this._saldo = this._saldo;
            console.log("\nTRANSAÇÃO RECUSADA: Saldo insuficiente.");
        }
        else if (novoSaldo >= -499, novoSaldo <= -1) {
            this._saldo = this._saldo + novoSaldo;
            console.log(`\nTransação de: ${novoSaldo}R$ aprovada`);
        }
        else {
            this._saldo = this._saldo + novoSaldo;
            console.log("\nValor guardado na conta de: " + this._nome);
        }

    }
}

console.log("\nSaldo disponível: " + conta._saldo)

conta.saldo = -500;

console.log("\nSaldo disponível: " + conta._saldo)

conta.saldo = 1000;

console.log("\nSaldo disponível: " + conta._saldo)

conta.saldo = -1100;

console.log("\nSaldo disponível: " + conta._saldo)