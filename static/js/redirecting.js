const loginButton = document.getElementById('login_button');
const historyButton = document.getElementById('history_button');

loginButton.addEventListener('click', () => {
    window.location.href = '/login';
});

historyButton.addEventListener('click', () => {
    window.location.href = '/history';
});