document.addEventListener("DOMContentLoaded", function() {
    const button = document.getElementById('trigger-button');
    
    button.addEventListener('click', function() {
        fetch('/trigger-script', {
            method: 'POST'
        }).then(response => {
            if (response.redirected) {
                // If the backend redirects to a success or error page
                window.location.href = response.url;
            } else {
                // If there's no redirection, send the user to an error page
                window.location.href = '/error';
            }
        }).catch(error => {
            alert('Error: ' + error.message);  // Optional error handling in case fetch itself fails
        });
    });
});