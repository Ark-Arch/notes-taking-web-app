// JavaScript to toggle the class on button click
function toggleText(button) {
	      var listItem = button.previousElementSibling;
	      var content = listItem.querySelector('.content');
	      content.classList.toggle('expanded');
	      //listItem.classList.toggle('expanded');
	      button.innerText = content.classList.contains('expanded') ? 'Read Less' : 'Read More';
}

// Add button dynamically to each list item
var listItems = document.querySelectorAll('.list-group-item');
listItems.forEach(function(item) {
	          var button = document.createElement('button');
	          button.setAttribute('class', 'expand-button');
	          button.innerText = 'Read More';
	          button.onclick = function() { toggleText(this); };
	          item.after(button);
  });
