function Pet(nome, especie, idade) {
    this.nome = nome,
    this.especie = especie,
    this.idade = idade
}

const orelhiniMacaquine = new Pet("Orelhini Macaquine", "cachorro", 3)
const mimi = new Pet("Mimi", "gato", 5)
const nemo = new Pet("Nemo", "peixe", 1)



console.log("\n", orelhiniMacaquine.nome);    // "Rex"
console.log("\n", mimi.especie);   // "gato"
console.log("\n", nemo.idade + 1, "\n");   // "2"
console.table(orelhiniMacaquine);    // "Rex", "cachorro", "3"