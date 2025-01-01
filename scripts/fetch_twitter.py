import tweepy
import json

def fetch_tweets(bearer_token, query, max_tweets=10):
    """
    Fetch recent tweets using Twitter API v2.

    Args:
        bearer_token (str): Bearer token for API authentication.
        query (str): Search query for tweets.
        max_tweets (int): Maximum number of tweets to fetch (1-100).

    Returns:
        None. Saves tweets to a JSON file.
    """
    # Authenticate with Twitter API v2
    client = tweepy.Client(bearer_token=bearer_token)

    # Fetch recent tweets
    response = client.search_recent_tweets(query=query, max_results=max_tweets, tweet_fields=['created_at'])

    # Parse tweets
    tweets = []
    if response.data:
        for tweet in response.data:
            tweets.append({
                "text": tweet.text,
                "created_at": str(tweet.created_at)
            })

    # Save tweets to a JSON file
    with open('./data/raw/twitter_data.json', 'w') as f:
        json.dump(tweets, f, indent=4)

    print(f"Fetched {len(tweets)} tweets for query '{query}'.")

# Replace with your Bearer Token
if __name__ == "__main__":
    fetch_tweets(
        bearer_token="AAAAAAAAAAAAAAAAAAAAAP5PxwEAAAAAFO2YihC5jmheQLf1zl2Ua5al5Zc%3DRwjhzica6l7MABcled5Npztl89Wb7scfwduNb7Z5YJt0QSrWjO",
        query="insurance",
        max_tweets=10
    )
