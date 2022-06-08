"use_strict"

function deletrear() {
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

function senar() {
    location.href = '/senar';
};

// function senar() {
//     const cam = document.querySelector('#camara');
//     const camContent = document.querySelector('#cam-content')

//     if (cam !== null) {
//         location.href = location.href;
//         alert('Cámara desactivada');
//     } else {
//         camContent.innerHTML = '<img src="/senas" class="m-5 rounded-3 border border-white border-3" id="camara">';
//         alert('Cámara activada');
//     }
// };