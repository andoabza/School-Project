var menu =  document.getElementById('menu');
var nav = document.getElementById('nav');
var close = document.getElementById('close');
menu.addEventListener('click', function() {
    nav.classList.remove('d-none');
    menu.classList.add('d-none');
    close.classList.remove('d-none');
    });
close.addEventListener('click', function() {
    nav.classList.add('d-none');
    menu.classList.remove('d-none');
    close.classList.add('d-none');
    });