'use strict';


var todoRequest = (function(){
  function todoRequest(callback) {
    var TODO_URL = 'http://localhost:3000/todos';
    $.ajax({
      url: TODO_URL,
      method: 'GET',
      // headers: ?,
      success: function(response){
        callback(response);
      }
    });
  }
  return todoRequest;
})();

//
// var xhr = new XMLHttpRequest();
// var url = 'http://localhost:3000/todos';
//
// xhr.open('GET', url, false);
// xhr.send();
//
//
//
//
// console.log(xhr.status);
// console.log(xhr.statusText);
