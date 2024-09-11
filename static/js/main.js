function triggerScript() {
	fetch('/trigger-script', {
		method: 'POST'
	}).then(response => {
		if (response.ok) {
			alert('Script executed successfully');
		} else {
			alert('Failed to execute script');
		}
	}).catch(error => {
		alert('Error: ' + error.message);
	});
}