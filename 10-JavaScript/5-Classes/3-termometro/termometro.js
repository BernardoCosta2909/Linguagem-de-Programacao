class Termometro {
    constructor(celsius) {
        this._celsius = celsius;
    }

    get celsius () {
        return this._celsius + "°C\n";
    }

    set celsius(valor) {
        if(valor < -50, valor > 60) {
            console.log("Temperatura inválida:", valor + "°C. Use um valor entre -50 e 60.\n")
        } else {
            this._celsius = valor;
            console.log("Temperatura ajustada para", this._celsius + "°C.\n")
        }
    }

    get fahrenheit () {
        return this._celsius * 9 / 5 + 32 + "°F\n"
    }
}

const t = new Termometro(20);

console.log(t.celsius);      // ?
console.log(t.fahrenheit);   // ?

t.celsius = 35;              // ?

console.log(t.fahrenheit);   // ?

t.celsius = 100;             // ?

console.log(t.celsius);      // ?