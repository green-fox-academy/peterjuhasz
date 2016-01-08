'use strict';

var kepek = [
    'http://lorempixel.com/512/384/sports/1/',
    'http://lorempixel.com/512/384/sports/2/',
    'http://lorempixel.com/512/384/sports/3/',
    'http://lorempixel.com/512/384/sports/5/',
    'http://lorempixel.com/512/384/sports/6/',
];
// ---------------------------------------------

var picture = document.querySelector('img');
var currentIndex = 0; //start value
var previousButton = document.querySelector('.stepback');
var nextButton = document.querySelector('.stepforward');
var thumbnailContainer = document.querySelector('.thumbnails');
var thumbnail = document.querySelector('.thumbnails');
var currentThumbnail = document.querySelector('.thumbnail'+ currentIndex);

function refreshTitle(id) {
    document.getElementById('title').innerHTML = 'Picture ' + id + '.';
}

function changePicture(src) {
    picture.setAttribute('src', src);
}

function generateThumbnails(pictures) {
    for (var i = 0; i < pictures.length; i++) {
        var thumbnail_img = document.createElement("img");
        thumbnail_img.src = pictures[i];
        thumbnail_img.setAttribute('class', i===0 ? 'current_img' : 'thumbnail')
        thumbnail_img.setAttribute('id','thumbnail'+ i)
        thumbnailContainer.appendChild(thumbnail_img)
    }
}

generateThumbnails(kepek);

previousButton.addEventListener('click',
    function () {
        document.getElementById('thumbnail'+currentIndex).setAttribute('class','thumbnail');

        if (currentIndex === 0 ) {
            previousButton.setAttribute('disabled','')
        }else {
            changePicture(kepek[--currentIndex]);
            refreshTitle(currentIndex+1);
            nextButton.removeAttribute('disabled');
        }

        document.getElementById('thumbnail'+currentIndex).setAttribute('class','current_img');
})

nextButton.addEventListener('click',
    function () {
        document.getElementById('thumbnail'+ currentIndex).setAttribute('class','thumbnail');
        
        if (currentIndex + 1 ===  kepek.length) {
            nextButton.setAttribute('disabled','');
        }else {
            changePicture(kepek[++currentIndex]);
            refreshTitle(currentIndex+1);
            previousButton.removeAttribute('disabled');
        }
        document.getElementById('thumbnail'+ currentIndex).setAttribute('class','current_img' );
    }
)

thumbnail.addEventListener('click',
    function () {
        console.log(event.target);
        var lightbox_container  = document.getElementById('lightbox');
        lightbox_container.setAttribute('class','show_lightbox');

        var lightboxImg = document.createElement("img");
        lightboxImg.src = event.target.src;
        lightboxImg.setAttribute('class', 'lightbox_image')
        lightbox_container.appendChild(lightboxImg);

        lightbox_container.addEventListener('click',
            function () {
                // console.log('under construction, refresh the page')
                lightboxImg.parentNode.removeChild(lightboxImg);
                lightbox_container.setAttribute('class','');
            }
        )
    }
)
