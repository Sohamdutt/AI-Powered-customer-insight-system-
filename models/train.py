import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_churn_model(data):
    # Define features and target for churn model
    X = data[['sentiment_score', 'temperature', 'trend_score']]
    y = data['purchase_likelihood']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Save churn model
    with open('./models/churn_model.pkl', 'wb') as f:
        pickle.dump(model, f)

    print("Churn model training complete. Model saved to './models/churn_model.pkl'.")

def train_sentiment_model(data):
    # Define features and target for sentiment model
    X = data[['sentiment_score']]
    y = data['purchase_likelihood']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Save sentiment model
    with open('./models/sentiment_model.pkl', 'wb') as f:
        pickle.dump(model, f)

    print("Sentiment model training complete. Model saved to './models/sentiment_model.pkl'.")

def train_weather_model(data):
    # Define features and target for weather model
    X = data[['temperature']]
    y = data['purchase_likelihood']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Save weather model
    with open('./models/weather_model.pkl', 'wb') as f:
        pickle.dump(model, f)

    print("Weather model training complete. Model saved to './models/weather_model.pkl'.")

if __name__ == "__main__":
    # Load processed data
    data = pd.read_csv('./data/processed/combined_data.csv')
    print("Columns in the dataset:", data.columns)

    # Train models
    train_churn_model(data)
    train_sentiment_model(data)
    train_weather_model(data)
