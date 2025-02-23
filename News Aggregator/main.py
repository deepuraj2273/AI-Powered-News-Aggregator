from fetch_news import fetch_news
from nlp_pipeline import preprocess_text, summarize_article, categorize_article
from store_news import store_news
def main():
    # Fetch the news articles
    articles = fetch_news()

    # Process the articles (summarize and categorize)
    processed_articles = []
    for article in articles:
        title = article['title']
        description = article['description'] if article['description'] else ""  # Handle NoneType
        url = article['url']
        published_at = article['publishedAt']
        
        if description.strip():  # Skip empty descriptions
            # Preprocess text
            preprocessed_text = preprocess_text(description)

            # Summarize article
            summary = summarize_article(preprocessed_text)

            # Categorize article
            category = categorize_article(preprocessed_text)

            # Append processed data
            processed_articles.append({
                "title": title,
                "summary": summary,
                "category": category,
                "url": url,
                "publishedAt": published_at
            })
    
    # Store processed news in JSON file
    if processed_articles:
        store_news(processed_articles)
    else:
        print("No valid articles found to process.")

if __name__ == "__main__":
    main()
