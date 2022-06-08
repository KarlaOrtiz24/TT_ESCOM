"use_strict"

let recognition = new webkitSpeechRecognition();
recognition.lang = 'es-MX';
recognition.continuous = true;
recognition.interimResults = false;
const grabar = document.querySelector('#btnGrabar');
const detener = document.querySelector('#btnDetener');
const traducir = document.querySelector('#btnTraducir');
const texto = document.querySelector('#texto');
const video = document.querySelector('#video');

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
        success: function (result) {
            texto.value = '';
            for (let clave in result) {
                let cad = '<video width="320" class="m-5 rounded-3 border border-white border-3" id="sena">' +
                            '<source src="' + "{{ url_for('static', filename='../static/BD/" + result[clave] +"') }}" + '" type="video/mp4">'
                            '</video>';
                video.innerHTML = cad;
                console.log(result[clave]);
            }
        }

    });

});
