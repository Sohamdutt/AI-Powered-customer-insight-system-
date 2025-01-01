from pytrends.request import TrendReq
import pandas as pd

def fetch_trends(keywords, timeframe='today 3-m', geo='US'):
    pytrends = TrendReq()
    pytrends.build_payload(keywords, timeframe=timeframe, geo=geo)

    trends = pytrends.interest_over_time()
    trends.to_csv('./data/raw/google_trends.csv', index=True)

    print("Google Trends data saved.")

if __name__ == "__main__":
    fetch_trends(
        keywords=["insurance", "health policy"],
        timeframe="today 3-m",
        geo="US"
    )
