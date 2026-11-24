class Lampada {
    constructor(comodo) {
        this.comodo = comodo,
        this.ligada = false
    }

    ligar() {
        if(this.ligada === true) {
            console.log("A luz da", this.comodo, "já está ligada.\n")
        } else {
            this.ligada = true;
            console.log("Luz da", this.comodo, "ligada.\n")
        }
    }

    desligar() {
        if(this.ligada === false) {
            console.log("A luz da", this.comodo, "já está desligada.\n")
        } else {
            this.ligada = false;
            console.log("Luz da", this.comodo, "desligada.\n")
        }
    }

    alternar () {
        if(this.ligada === true) {
            this.desligar()
        } else {
            this.ligar()
        }
    }
}

const sala = new Lampada("sala");
const cozinha = new Lampada("cozinha");

sala.ligar();          // liga
sala.ligar();          // já está ligada

cozinha.alternar();    // liga
cozinha.alternar();    // desliga
cozinha.desligar();    // já está desligada

console.log("Sala:", sala.ligada, "Cozinha:" ,cozinha.ligada);  // true e false