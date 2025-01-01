import pandas as pd
import json
import random

def preprocess():
    # Load Twitter data
    with open('./data/raw/twitter_data.json', 'r') as f:
        twitter_data = pd.DataFrame(json.load(f))
        twitter_data['sentiment_score'] = twitter_data['text'].apply(lambda x: len(x.split()))  # Example feature

    # Load Weather data
    with open('./data/raw/weather_Mumbai.json', 'r') as f:
        weather_data_json = json.load(f)

    # Check if 'main' key exists in weather JSON
    if 'main' in weather_data_json and 'weather' in weather_data_json:
        weather_data = pd.DataFrame([{
            "temperature": weather_data_json['main']['temp'],
            "weather_description": weather_data_json['weather'][0]['description']
        }])
    else:
        print("Error: Weather data does not contain expected keys.")
        weather_data = pd.DataFrame([{"temperature": None, "weather_description": None}])

    # Load Google Trends data
    trends_data = pd.read_csv('./data/raw/google_trends.csv')

    # Extract trend scores (example: sum or average of trends for specific keywords)
    trends_data['trend_score'] = trends_data[['insurance', 'health policy']].mean(axis=1)

    # Combine datasets (basic merge example)
    combined = pd.concat([twitter_data, weather_data.reset_index(drop=True), trends_data[['trend_score']].reset_index(drop=True)], axis=1)

    # Add a placeholder purchase_likelihood column (simulated for this example)
    combined['purchase_likelihood'] = combined['sentiment_score'].apply(lambda x: 1 if x > 5 else 0)

    # Save processed data
    combined.to_csv('./data/processed/combined_data.csv', index=False)
    print("Data preprocessing complete. Combined data saved.")

if __name__ == "__main__":
    preprocess()
