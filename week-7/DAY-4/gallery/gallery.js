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
    'http://lorempixel.com/400/200/sports/12/'
];
// ---------------------- Buttons -----------------------

var picture = document.querySelector('img');
var currentIndex = 0;
var previousButton = document.querySelector('.stepback');
var nextButton = document.querySelector('.stepforward');
// var title = document.getElementById('title');

// document.getElementById('title').innerHTML = 'alma';

function refreshTitle(id) {
    document.getElementById('title').innerHTML = 'Picture ' + id + '.';
}

function changePicture(src) {
    picture.setAttribute('src', src)
}

previousButton.addEventListener('click',
    function () {
        currentIndex === 0 ? alert('this is the first picture') : (changePicture(kepek[--currentIndex]), refreshTitle(currentIndex+1));
})

nextButton.addEventListener('click',
    function () {
        currentIndex + 1 ===  kepek.length ? alert('this is the last picture') : (changePicture(kepek[++currentIndex]), refreshTitle(currentIndex+1));
})
//-------------------Refactoring-------------------------
// previousButton.addEventListener('click',
//     function () {
//         if (currentIndex === 0) {
//             alert('this is the first picture')
//         }else {
//             changePicture(kepek[--currentIndex]);
//             refreshTitle(currentIndex+1);
//         }
// })
// nextButton.addEventListener('click',
//     function () {
//         if (currentIndex + 1 === kepek.length) {
//             alert('this is the first picture')
//         }else {
//             changePicture(kepek[++currentIndex]);
//             refreshTitle(currentIndex+1);
//         }
// })






//
