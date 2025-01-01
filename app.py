from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load models
try:
    with open('./models/churn_model.pkl', 'rb') as f:
        churn_model = pickle.load(f)
    with open('./models/sentiment_model.pkl', 'rb') as f:
        sentiment_model = pickle.load(f)
    with open('./models/weather_model.pkl', 'rb') as f:
        weather_model = pickle.load(f)
except Exception as e:
    print(f"Error loading models: {e}")

# Root route
@app.route('/')
def home():
    # Render your dashboard HTML or return a welcome message
    return render_template('dashboard.html')

@app.route('/predict_churn', methods=['POST'])
def predict_churn():
    data = request.json
    df = pd.DataFrame([data])
    prediction = churn_model.predict(df)
    return jsonify({'churn_prediction': prediction.tolist()})

@app.route('/predict_sentiment', methods=['POST'])
def predict_sentiment():
    data = request.json
    df = pd.DataFrame([data])
    prediction = sentiment_model.predict(df)
    return jsonify({'sentiment_prediction': prediction.tolist()})

@app.route('/predict_weather', methods=['POST'])
def predict_weather():
    data = request.json
    df = pd.DataFrame([data])
    prediction = weather_model.predict(df)
    return jsonify({'weather_prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
