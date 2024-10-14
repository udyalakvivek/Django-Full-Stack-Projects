document.addEventListener('DOMContentLoaded', function () {
    var navbar = document.querySelector('.my-navbar');
    var navOffset = navbar.offsetTop;
    window.addEventListener('scroll', function () {
        if (window.scrollY > navOffset) {
            navbar.classList.add('fixed-nav')
        }
        else {
            navbar.classList.remove('fixed-nav')
        }
    });

});
