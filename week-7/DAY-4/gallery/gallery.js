'use strict';

var kepek = [
    'http://lorempixel.com/400/200/sports/1/',
    'http://lorempixel.com/400/200/sports/2/',
    'http://lorempixel.com/400/200/sports/3/',
    'http://lorempixel.com/400/200/sports/5/',
    'http://lorempixel.com/400/200/sports/6/',
    'http://lorempixel.com/400/200/sports/7/',
    'http://lorempixel.com/400/200/sports/8/',
    'http://lorempixel.com/400/200/sports/9/',
    'http://lorempixel.com/400/200/sports/11/'
];
// ---------------------- Buttons -----------------------

var picture = document.querySelector('img');
var currentIndex = 0;
var previousButton = document.querySelector('.stepback');
var nextButton = document.querySelector('.stepforward');


function changePicture(src) {
    picture.setAttribute('src', src)
}

previousButton.addEventListener('click',
function () {
    changePicture(kepek[--currentIndex]);
})

nextButton.addEventListener('click',
function () {
    changePicture(kepek[++currentIndex]);
})






//
