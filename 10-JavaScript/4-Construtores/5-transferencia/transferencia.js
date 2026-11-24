function Conta(dono, saldo) {
    this.dono = dono;
    this.saldo = saldo;

    this.mostrar = function () {
        console.log(this.dono, "tem", this.saldo, "R$\n")
    },

        this.transferir = function (destino, valor) {

            this.mostrar()
            destino.mostrar()

            if (valor > this.saldo) {
                console.log("O saldo do(a)", this.dono, "é insuficiente! Valor da tentativa de transfêrencia:", valor, "R$. Saldo atual:", this.saldo, "R$\n")
            } else {
                this.saldo -= valor;
                destino.saldo += valor;


                console.log(this.dono, "transferiu", valor, "R$ para", destino.dono, "\n")
            }

        }
}

const ana = new Conta("Ana", 100)
const beto = new Conta("Beto", 50)

ana.transferir(beto, 30);   // ?
beto.transferir(ana, 200);  // ?
