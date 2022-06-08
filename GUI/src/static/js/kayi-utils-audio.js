"use_strict"

let recognition = new webkitSpeechRecognition();
recognition.lang = 'es-MX';
recognition.continuous = true;
recognition.interimResults = false;
const grabar = document.querySelector('#btnGrabar');
const detener = document.querySelector('#btnDetener');
const traducir = document.querySelector('#btnTraducir');
const texto = document.querySelector('#texto');

recognition.onresult = (e) => {
    const result = e.results;
    const frase = result[result.length - 1][0].transcript;
    texto.value += frase;
};

recognition.onend = (e) => {
    alert('He dejado de reconocer');
}

grabar.addEventListener('click', (err) => {
    alert('He iniciado el reconocimiento');
    grabar.classList.add('btn_selection_selected');
    grabar.disabled = true;
    detener.disabled = false;
    audioGrabado = [];
    recognition.start();
});

detener.addEventListener('click', (err) => {
    grabar.classList.remove('btn_selection_selected');
    grabar.disabled = false;
    detener.disabled = true;
    recognition.stop();

    // let data = { 'texto': $('#texto').val() };
    
    $.ajax({
        
        type: 'POST',
        url: '/traducir',
        data: JSON.stringify($('#texto').val()),
        success: function(result){
            texto.value = '';
            console.log(result);
        }

    });

});
