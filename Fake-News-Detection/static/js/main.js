// static/js/main.js

document.getElementById('newsForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const newsText = document.getElementById('newsText').value;

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: 'news_text=' + encodeURIComponent(newsText)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').textContent = data.result;
    });
});
