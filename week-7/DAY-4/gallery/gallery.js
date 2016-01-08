'use strict';

var kepek = [
    'http://lorempixel.com/512/384/sports/1/',
    'http://lorempixel.com/512/384/sports/2/',
    'http://lorempixel.com/512/384/sports/3/',
    'http://lorempixel.com/512/384/sports/5/',
    'http://lorempixel.com/512/384/sports/6/',
];
// ----------------------w-----------------------

var picture = document.querySelector('img');
var currentIndex = 0;
var previousButton = document.querySelector('.stepback');
var nextButton = document.querySelector('.stepforward');
var thumbnailContainer = document.querySelector('.thumbnails');

function refreshTitle(id) {
    document.getElementById('title').innerHTML = 'Picture ' + id + '.';
}

function changePicture(src) {
    picture.setAttribute('src', src)
}

generateThumbnails(kepek);

previousButton.addEventListener('click',
    function () {
        document.getElementById('thumbnail'+currentIndex).setAttribute('class','thumbnail');

        currentIndex === 0 ? previousButton.setAttribute('disabled','') : (changePicture(kepek[--currentIndex]),
        refreshTitle(currentIndex+1),
        nextButton.removeAttribute('disabled'));

        document.getElementById('thumbnail'+currentIndex).setAttribute('class','current_img');
})

nextButton.addEventListener('click',
    function () {
        // var currentThumbnail = document.getElementById('thumbnail'+currentIndex);

        document.getElementById('thumbnail'+currentIndex).setAttribute('class','thumbnail');

        currentIndex + 1 ===  kepek.length ? nextButton.setAttribute('disabled','') : (changePicture(kepek[++currentIndex]),
        refreshTitle(currentIndex+1),
        previousButton.removeAttribute('disabled'));
        // generateThumbnails(kepek);

        document.getElementById('thumbnail'+currentIndex).setAttribute('class','current_img' );
})

function generateThumbnails(pictures) {
    for (var i = 0; i < pictures.length; i++) {
        var thumbnail_img = document.createElement("img");
        thumbnail_img.src = kepek[i];
        thumbnail_img.style.width = '102.4px';
        thumbnail_img.style.height = '76.8px';
        thumbnail_img.setAttribute('class','thumbnail')
        thumbnail_img.setAttribute('id','thumbnail'+ i)
        thumbnailContainer.appendChild(thumbnail_img)
    }
}

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
