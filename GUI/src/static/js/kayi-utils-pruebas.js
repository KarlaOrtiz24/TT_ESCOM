"use_strict"

// import { MediaRecorder, register } from 'extendable-media-recorder';
// import { connect } from 'extendable-media-recorder-wav-encoder';

const grabar = document.querySelector('#btnGrabar');
const detener = document.querySelector('#btnDetener');
// const traducir = document.querySelector('#btnTraducir');
const grabacion = document.querySelector('#grabacion');

navigator.mediaDevices.getUserMedia({ audio: true })
    .then((stream) => {
        handlerFunction(stream);
    });

function handlerFunction(stream) {
    rec = new MediaRecorder(stream);
    rec.ondataavailable = (e) => {
        audioGrabado.push(e.data);
        if (rec.state == 'inactive') {
            let blob = new Blob(audioGrabado, { type: 'audio/wav; codecs="MS_PCM"' });
            grabacion.src = URL.createObjectURL(blob);
            grabacion.controls = true;
            grabacion.autoplay = true;

            const data = new FormData();
            data.append('file', blob, 'file');

            fetch('/traducir', {
                method: 'POST',
                body: data
            }).then(response => response.json()
            ).then(json => {
                console.log(json);
            });

        }
    };
};

grabar.addEventListener('click', (err) => {
    // console.log('Iniciar grabación');
    grabar.classList.add('btn_selection_selected');
    grabar.disabled = true;
    detener.disabled = false;
    audioGrabado = [];
    rec.start();
});

detener.addEventListener('click', (err) => {
    // console.log('Detener grabación');
    grabar.classList.remove('btn_selection_selected');
    grabar.disabled = false;
    detener.disabled = true;
    rec.stop();
});

