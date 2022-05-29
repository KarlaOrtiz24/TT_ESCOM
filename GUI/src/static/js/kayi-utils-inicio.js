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

// function ajax() {
//     const http = new XMLHttpRequest();
//     const url = 'http://localhost:5000/carga';

//     if()
// };