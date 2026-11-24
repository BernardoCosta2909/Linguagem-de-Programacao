const nomeAna = document.getElementById("nome-ana");
const pontosAna = document.getElementById("pontos-ana");

const nomeBeto = document.getElementById("nome-beto");
const pontosBeto = document.getElementById("pontos-beto");

const nomeBernardo = document.getElementById("nome-bernardo");
const pontosBernardo = document.getElementById("pontos-bernardo");

function Jogador(nome, id) {
    this.nome = nome,
    this.pontos = 0,
    this.id = id,

    this.atualizarTela = function() {
        nomeAna.textContent = this.nome;
        pontosAna.textContent = this.pontos;
        nomeBeto.textContent = this.nome;
        pontosBeto.textContent = this.pontos;
        nomeBernardo.textContent = this.nome;
        pontosBernardo.textContent = this.pontos;
    },

    this.marcar = function() {
        this.pontos += 1;
        this.atualizarTela()
    }
}

const ana = new Jogador.atualizarTela("Ana")
const beto = new Jogador.atualizarTela("Beto")
const bernardo = new Jogador.atualizarTela("Bernardo")

document.getElementById("botao-ana").addEventListener("click", function () {
  ana.marcar();
});

document.getElementById("botao-beto").addEventListener("click", function () {
  beto.marcar();
});

document.getElementById("botao-bernardo").addEventListener("click", function () {
  bernardo.marcar();
});