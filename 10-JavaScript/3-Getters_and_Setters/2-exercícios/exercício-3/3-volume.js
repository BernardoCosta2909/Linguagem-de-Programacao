console.log("--- Volume ---")

const celular = {

    _volume: 50,

    get volume() {
        return this._volume
    },

    set volume(novoVolume) {
        if (typeof novoVolume !== "number") {
            console.log("\nERRO: O volume precisa ser um número");
        }

        if (novoVolume < 0) {
            this._volume = 0;
            console.log("\nVolume no mínimo (0)")
        }
        else if (novoVolume > 100) {
            this._volume = 100;
            console.log("\nVolume no máximo (100)");
        }
        else {
            this._volume = this._volume + novoVolume
            console.log("\nVolume: " + this._volume);
        }

    }
}

celular.volume += 20;
celular.volume += 50;
celular.volume -= 30;
celular.volume = -10;
celular.volume = "alto";
console.log("Volume final: ", celular.volume);