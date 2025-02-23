# fetch_news.py

import requests

NEWS_API_KEY = "d60921f9faac4e85bfc49b02b2525060"
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

def fetch_news():
    # Fetch news from NewsAPI
    response = requests.get(NEWS_API_URL, params={"apiKey": NEWS_API_KEY, "country": "us"})
    articles = response.json()['articles']
    
    news_data = []
    for article in articles:
        title = article['title']
        description = article['description']
        url = article['url']
        published_at = article['publishedAt']
        news_data.append({
            "title": title,
            "description": description,
            "url": url,
            "publishedAt": published_at
        })
    
    return news_data
