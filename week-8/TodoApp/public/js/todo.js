'use strict'


var refreshButton = document.querySelector('#refresh-btn');
var mainContainer = document.querySelector('.main-container');

refreshButton.addEventListener('click', function () {
  console.log('megnyomtad a gombot');

  todoRequest(function (todoList) {
    console.log(todoList);
    fillMainContainer(todoList);
  });
})

function fillMainContainer(listElements) {
  for (var i = 0; i < listElements.length; i++) {
    var todoItem = document.createElement("div");

    setAttrForPriority(listElements, todoItem, i)
    // console.log(listElements[i]);
    todoItem.setAttribute('data-custom-order', 6+i); //NOTE: for add button use listElements.length+1
    todoItem.setAttribute('style', "display: block;");
    todoItem.innerHTML = listElements[i].text;
    console.log(todoItem);
    mainContainer.appendChild(todoItem);
  }
}

function setAttrForPriority(listElements, todoItem, i) { //TODO:
  if (listElements[i].priority === 'low') {
    todoItem.setAttribute('class','mix low');
  }else if (listElements[i].priority === 'medium') {
    todoItem.setAttribute('class','mix medium');
  }else {
    todoItem.setAttribute('class','mix high');
  }
}
