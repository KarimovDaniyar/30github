// static/js/login.js
document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');
    const messageDiv = document.getElementById('message');

    loginForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        
        fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                messageDiv.textContent = data.message;
                messageDiv.className = 'success-message';
                setTimeout(() => {
                    window.location.href = '/dashboard';
                }, 2000);
            } else {
                messageDiv.textContent = data.message;
                messageDiv.className = 'error-message';
            }
        })
        .catch(error => {
            messageDiv.textContent = 'Произошла ошибка: ' + error;
            messageDiv.className = 'error-message';
        });
    });
});