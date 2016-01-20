'use strict';

// var refreshRequest = (function(){
//   function refreshRequest(callback) {
//     var TODO_URL = 'http://localhost:3000/todos';
//     $.ajax({
//       url: TODO_URL,
//       method: 'GET',
//       success: function(response){
//         callback(response);
//       }
//     });
//   }
//   return refreshRequest;
// })();


// var TODO_URL = 'http://localhost:3000/todos';
// function requestTemplate(id, method, callback){
//   $.ajax({
//     url: TODO_URL + id,
//     method: method,
//     success: function(response){
//       callback(response);
//     }
//   });
// }

function getRequest(callback) {
  var TODO_URL = 'http://localhost:3000/todos';
  $.ajax({
    url: TODO_URL,
    method: 'GET',
    success: function(response){
      callback(response);
    }
  });
}

function deleteRequest(id) {
  $.ajax({
    url: 'http://localhost:3000/todos/'+id,
    method: 'DELETE',
    data: undefined,
    success: function(response){
      console.log(response);
    }
  });
  // refreshRequest();
}

function postRequest() {
  $.ajax({
    url: 'http://localhost:3000/todos',
    method: 'POST',
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify({text: 'teszt', priority: 'medium'}),
    success: function(response){
      console.log('response: ', response);
    }
  });
  refreshRequest();
}
