function toggleContent() {
	    var content = document.getElementById('full-content');
	    var button = document.getElementById('toggle-button');
	    
	    if (content.style.display === 'none' || content.style.display === '') {
		            content.style.display = 'block';
		            button.innerText = 'View less';
	     } else {
	        content.style.display = 'none';
	        button.innerText = 'View more';
	    }
}
