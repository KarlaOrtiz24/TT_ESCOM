"use_strict"

const ul = document.querySelector('ul');

function frames() {

    const animacion = ul.animate([
        { transform: 'TranslateY(0rem)' },
        { transform: 'TranslateY(-2.5rem)' }
    ], {
        easing: 'linear',
        iterations: 1,
        duration: 200
    });

    return animacion.finished;
};

function displace() {
    frames().then((res) => {
        console.log(res);
        ul.appendChild(document.querySelectorAll('ul > li')[0]);
    });
};

setInterval(() => {
    displace();
}, 1500);