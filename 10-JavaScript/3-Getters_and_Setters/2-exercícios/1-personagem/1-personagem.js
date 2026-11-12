console.log("--- RPG ---")

const personagem = {

    _nome: "Cyber Ninja",
    _hp: 100,

    get hp() {
        return this._hp
    },

    set hp(novoHp) {
        if (novoHp <= 0) {
            this._hp = 0;
            console.log("\nGAME OVER");
        }

        else if (novoHp >= 100) {
            this._hp = 100;
            console.log("\nVida máxima atingida");
        }

        else {
            this._hp = novoHp;
            console.log(`\nHP atualizado para ${this._hp}`);
        }
    }
}

console.log("\nnome do personagem: " + personagem._nome)
console.log("\nvida inicial do personagem: " + personagem.hp)
console.log("\n--- Início do jogo ---")

personagem.hp = 150;
personagem.hp = 45;
personagem.hp = -20;