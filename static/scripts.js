document.getElementById('churn-btn').addEventListener('click', () => {
    const data = { sentiment_score: 10, temperature: 25, trend_score: 80 }; // Example input
    fetch('/predict_churn', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
    })
        .then((response) => response.json())
        .then((result) => {
            document.getElementById('output').innerText = `Churn Prediction: ${result.churn_prediction}`;
        });
});

document.getElementById('sentiment-btn').addEventListener('click', () => {
    const data = { sentiment_score: 15 }; // Example input
    fetch('/predict_sentiment', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
    })
        .then((response) => response.json())
        .then((result) => {
            document.getElementById('output').innerText = `Sentiment Prediction: ${result.sentiment_prediction}`;
        });
});

document.getElementById('weather-btn').addEventListener('click', () => {
    const data = { temperature: 30 }; // Example input
    fetch('/predict_weather', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
    })
        .then((response) => response.json())
        .then((result) => {
            document.getElementById('output').innerText = `Weather Prediction: ${result.weather_prediction}`;
        });
});
