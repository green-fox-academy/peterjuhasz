'use strict'


var addButton = document.querySelector('#add-btn');
var doneButton = document.querySelector('#done-btn');
var deleteButton = document.querySelector('#delete-btn');
var refreshButton = document.querySelector('#refresh-btn');

var mainContainer = document.querySelector('.main-container');
//==============================================================
addButton.addEventListener('click', function () {
  newItem()
  console.log('add');
})

doneButton.addEventListener('click', function () {
  console.log('done');
})

deleteButton.addEventListener('click', function () {
  deleteItem();
})

refreshButton.addEventListener('click', function () {
  // // console.log('megnyomtad a gombot');
  refreshItems();
})
//==============================================================
function refreshItems(){
  getRequest(function (todoList) {
    fillMainContainer(todoList);
  });
}

function newItem(argument) {
  postRequest('proba', 'low', refreshItems)
}

function deleteItem(){
  var itemsToDelete = document.querySelectorAll('.checkbox');
  for (var i = 0; i < itemsToDelete.length; i++) {
    if (itemsToDelete[i].checked===true) {
      console.log(parseInt(itemsToDelete[i].id));
      deleteRequest(parseInt(itemsToDelete[i].id), refreshItems)
    }
  }
}

function fillMainContainer(listElements) {
  mainContainer.innerHTML = "";
  for (var i = 0; i < listElements.length; i++) {
    var todoItem = document.createElement("div");
    setAttrForPriority(listElements, todoItem, i)
    // console.log(listElements[i]);
    todoItem.setAttribute('data-custom-order', listElements[i].id);
    todoItem.setAttribute('style', "display: block;");
    todoItem.innerHTML = listElements[i].id + '.' + listElements[i].text + '<input type="checkbox" class="checkbox" id='+listElements[i].id+'>';
    console.log(todoItem);
    mainContainer.appendChild(todoItem);
  }
}

function setAttrForPriority(listElements, todoItem, i) {
  if (listElements[i].priority === 'low') {
    todoItem.setAttribute('class','mix low');
  }else if (listElements[i].priority === 'medium') {
    todoItem.setAttribute('class','mix medium');
  }else {
    todoItem.setAttribute('class','mix high');
  }
}
