"use-strict"

var TodoItem = function () {
  this.id = nextId();
  this.priority = "";
  this.text = "";
  this.completed = false;
  // this.date = "";
}

TodoItem.prototype.update = function(attributes) {
  this.text = attributes.text || "";
  this.priority = attributes.priority || "";
  this.completed = !!attributes.completed;
};

var currId = 0;
function nextId() {
  return ++currId;
}

var items = {};

function getItem(id) {
  return items[id];
}

function addItem(attributes) {
  var item = new TodoItem();
  item.update(attributes);
  items[item.id] = item;
  return item;
}

function removeItem(id) {
  delete items[id];
}

function allItems() {
  var values = [];
  for (id in items) {
    values.push(items[id]);
  }
  return values;
}

module.exports = {
  get: getItem,
  add: addItem,
  remove: removeItem,
  all: allItems,
};
