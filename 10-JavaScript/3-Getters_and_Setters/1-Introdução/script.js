console.log("--- CONTROLE DO AR-CONDICIONADO ---");

const arCondicionado = {

    _temperatura: 24,

    get temperatura() {
        return this._temperatura;
    },

    set temperatura(novoValor) {
        if (novoValor < 16) {
            console.log("ERRO: O ar não gela abaixo de 16°C!");
        }

        else if (novoValor > 30) {
            console.log("ERRO: O ar não aquece acima de 30°C!");
        }

        else {
            this._temperatura = novoValor;
            console.log(`Temperatura ajustada para ${this._temperatura}°C`);
        }
    }
};

arCondicionado.temperatura = 12;
arCondicionado.temperatura = 35;
arCondicionado.temperatura = 22;