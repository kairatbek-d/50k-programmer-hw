document.addEventListener('DOMContentLoaded', () => {

    var myInterval = undefined;

    if ('counter' in localStorage) {
        const txt = document.getElementsByTagName('div')[0]
        txt.innerText = localStorage.getItem('counter')
    }

    let btnStart = document.querySelector('button')
    btnStart.addEventListener('click', () => {
        myInterval = setInterval(() => {
            var txt = document.getElementById('counter')
            txt.innerText = Number(txt.innerText) + 1
            localStorage.setItem('counter', txt.innerText)
        }, 1000);
    })

    let btnStop = document.querySelectorAll('button')[1]
    btnStop.addEventListener('click', () => {
        clearInterval(myInterval)
    })

    let btnClear = document.querySelectorAll('button')[2]
    btnClear.addEventListener('click', () => {
        clearInterval(myInterval)
        const txt = document.getElementsByTagName('div')[0]
        txt.innerText = 0
        localStorage.removeItem('counter')
    })
})