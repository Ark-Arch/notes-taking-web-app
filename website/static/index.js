function deleteNote(noteId) {
	fetch('/delete-note',  {
		method: 'POST',
		body: JSON.stringify({ noteId: noteId})
	}).then((_res) => {
		window.location.href="/previous-notes"; //basically refreshes the home page.
	});
}

