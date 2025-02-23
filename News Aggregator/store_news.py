# store_news.py

import json

def store_news(news_data, filename="processed_news.json"):
    with open(filename, "w") as f:
        json.dump(news_data, f, indent=4)
