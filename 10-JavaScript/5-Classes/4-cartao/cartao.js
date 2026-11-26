class CartaoTransporte {
    #saldo = 0;

    constructor(dono, tarifa) {
        this.dono = dono,
        this.tarifa = tarifa
    };

    get saldo() {
        return this.#saldo + "\n"
    };

    get extrato() {
        return this.dono + ": R$" + this.#saldo.toFixed(2) + "\n"
    };

    recarregar(valor) {
        if(valor <= 0) {
            console.log("Recarga inválida:", valor + ". Informe um valor maior que zero.\n")
        } else {
            this.#saldo += valor;
            console.log("Recarga de R$" + valor.toFixed(2) + ".", this.extrato, "\n")
        }
    };

    passar() {
        if(this.#saldo < this.tarifa) {
            console.log("Saldo insuficiente para", this.dono + ". Faltam R$" + (this.tarifa - this.#saldo), "\n")
        } else {
            this.#saldo -= this.tarifa;
            console.log("Catraca liberada.", this.dono + ": R$" + this.#saldo, "\n")
        }
    }
}

const bernardo = new CartaoTransporte("Bernardo", 5.5);

console.log(bernardo.saldo);
bernardo.passar();                // ?
bernardo.recarregar(10);          // ?
bernardo.passar();                // ?
bernardo.recarregar(-5);          // ?
bernardo.saldo = 1000;            // ?
console.log(bernardo.saldo);      // ?
bernardo.tarifa = 0.01;           // ?
bernardo.passar();                // ?
console.log(bernardo.extrato);    // ?

// Deixe esta última linha comentada por enquanto:
// console.log(bernardo.#saldo);