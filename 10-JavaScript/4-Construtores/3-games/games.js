function Jogador(nome) {
    this.nome = nome,
    this.pontos = 0,

    this.marcar = function (qtd) {
        this.pontos += qtd;
        console.log(this.nome, " marcou ", qtd, " pontos. Total: ", this.pontos, "\n")
    }
}

const ana = new Jogador("Ana")
const beto = new Jogador("Beto")
const bernardo = new Jogador("Bernardo")

ana.marcar(3);             // 3
beto.marcar(2);            // 2
ana.marcar(5);             // 6
bernardo.marcar(67);       // 67

console.log(ana.pontos, "\n");   // 6
console.log(beto.pontos, "\n");  // 3
console.log(bernardo.pontos, "\n");  // 67

console.table(ana)
console.table(beto)
console.table(bernardo)