"use_strict"

function camara() {
    const cam = document.querySelector('#camara');
    const camContent = document.querySelector('#cam-content')

    if (cam !== null) {
        location.href = location.href;
        alert('Cámara desactivada');
    } else {
        camContent.innerHTML = '<img src="/camara" class="m-5 rounded-3 border border-white border-3" id="camara">';
        alert('Cámara activada');
    }
};

function micro() {
    let recognition = new webkitSpeechRecognition();
    recognition.lang = 'es-MX';
    recognition.continuous = true;
    recognition.interimResults = false;
    const mic = document.querySelector('#btnMicro');
    const texto = document.querySelector('#texto');

    recognition.onresult = (e) => {
        const result = e.results;
        const frase = result[result.length - 1][0].transcript;
        texto.innerText = frase;
    };

    if (mic.value === '0') {
        mic.value = '1';
        mic.classList.remove('menu_shape_btn');
        mic.classList.add('btn_active');
        recognition.start();
    } else if (mic.value === '1') {
        mic.value = '0';
        mic.classList.remove('btn_active');
        mic.classList.add('menu_shape_btn');
        recognition.stop();
    }
};

// function ajax() {
//     const http = new XMLHttpRequest();
//     const url = 'http://localhost:5000/carga';

//     if()
// };