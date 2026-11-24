class Pet {
    constructor(nome, especie, idade) {
        this.nome = nome,
        this.especie = especie,
        this.idade = idade
    };

    apresentar() {
        return "Oi, eu sou o(a)" + " " + this.nome + ". Espécie:" + " " + this.especie + ", idade:" + " " + this.idade + ".\n"
    }
}

const orelha = new Pet("Orelha", "cachorro", 3)
const mimi = new Pet("Mimi", "gato", 5)
const nemo = new Pet("Nemo", "peixe", 1)

console.log(orelha.apresentar());          // Oi, eu sou o(a) Orelha! Espécie: cachorro, idade: 3.
console.log(mimi.apresentar());         // Oi, eu sou o(a) Mimi! Espécie: gato, idade: 5.
console.log(nemo.apresentar());         // Oi, eu sou o(a) Nemo! Espécie: peixe, idade: 1.

console.log(typeof Pet);                // function

const bob = Pet("Bob", "cachorro", 2);  // vai dar erro