function Heroi(nome) {
    this.nome = nome,
        this.vida = 100,

        this.mostrarStatus = function () {
            console.log(this.nome, "está com", this.vida, "de vida.\n")
        },

        this.levarDano = function (dano) {
            this.vida -= dano;

            if (this.vida <= 0) {
                this.vida = 0;
                console.log(this.nome, "foi derrotado!\n");
            } else { 
                this.mostrarStatus() 
            }
        }
}

const link = new Heroi("Link")
const zelda = new Heroi("Zelda")

link.levarDano(30);    // 70
zelda.levarDano(50);   // 50
link.levarDano(80);    // derrotado
zelda.mostrarStatus(); // ?

console.table(link)
console.table(zelda)