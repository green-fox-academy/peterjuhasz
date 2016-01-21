'use strict';
function customRequest(id, method, callback) {
  var TODO_URL = 'http://localhost:3000/todos/'+id;
  $.ajax({
    url: TODO_URL,
    method: method,
    success: function(response){
      return callback(response);
    }
  });
}


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

function putRequest(id, text, priority, completed, callback) {
  $.ajax({
    url: 'http://localhost:3000/todos/' + id,
    method: 'PUT',
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify({text: text, priority: priority, completed: completed}),
    success: function(response){
      console.log('response');
      callback();
    }
  });
}
