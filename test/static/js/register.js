// static/js/register.js
document.addEventListener('DOMContentLoaded', function() {
    const registerForm = document.getElementById('registerForm');
    const messageDiv = document.getElementById('message');

    registerForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const username = document.getElementById('username').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        
        fetch('/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: username,
                email: email,
                password: password
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                messageDiv.textContent = data.message;
                messageDiv.className = 'success-message';
                setTimeout(() => {
                    window.location.href = '/login';
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

