'use strict';

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

function deleteRequest(id, callback) {
  $.ajax({
    url: 'http://localhost:3000/todos/'+id,
    method: 'DELETE',
    data: undefined,
    success: function(response){
      callback();
    }
  });
}

function postRequest(text, priority, callback) {
  $.ajax({
    url: 'http://localhost:3000/todos',
    method: 'POST',
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify({text: text, priority: priority}),
    success: function(response){
      callback();
    }
  });
}
