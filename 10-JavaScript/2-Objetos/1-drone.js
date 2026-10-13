const drone = {

    modelo: 'scaryghost 2000',
    bateria: 100,
    cameraLigada: false,

    ativarCamera() {
        this.cameraLigada = true;

        console.log("câmera do drone " + this.modelo + ", com " + this.bateria + "% de bateria," + " " + this.cameraLigada + "!")
    }
}

drone.ativarCamera()