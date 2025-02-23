# app.py

import streamlit as st
import json

# Load the processed news from JSON file
def load_news(filename="processed_news.json"):
    with open(filename, "r") as f:
        return json.load(f)

# Display the news articles using Streamlit
def display_news(news_data):
    st.title("AI News Aggregator")

    # Create a dropdown to filter by category
    categories = list(set([article['category'] for article in news_data]))
    selected_category = st.selectbox("Select a category", categories)

    filtered_news = [article for article in news_data if article['category'] == selected_category]

    for article in filtered_news:
        st.subheader(article['title'])
        st.write(f"**Category**: {article['category']}")
        st.write(f"**Published**: {article['publishedAt']}")
        st.write(article['summary'])
        st.write(f"[Read More]({article['url']})")

# Main function
def main():
    # Load and display processed news
    news_data = load_news()
    display_news(news_data)

if __name__ == "__main__":
    main()

