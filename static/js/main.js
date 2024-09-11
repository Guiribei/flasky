document.addEventListener("DOMContentLoaded", function() {
    const button = document.getElementById('trigger-button');
    
    button.addEventListener('click', function() {
        fetch('/trigger-script', {
            method: 'POST'
        }).then(response => {
            if (response.redirected) {
                window.location.href = response.url;
            } else {
                alert('Failed to execute script');
            }
        }).catch(error => {
            alert('Error: ' + error.message);
        });
    });
});