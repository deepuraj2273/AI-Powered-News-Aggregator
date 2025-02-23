# nlp_pipeline.py

import spacy
from transformers import pipeline

# Load spaCy model for preprocessing
nlp = spacy.load("en_core_web_sm")

# Define Summarization and Categorization Models
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def preprocess_text(text):
    # Clean text using spaCy (tokenization, lemmatization, remove stopwords)
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])

def summarize_article(article_text):
    # Summarize the article using BART
    summary = summarizer(article_text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']

def categorize_article(article_text):
    candidate_labels = [
        "Politics", "Business", "Technology", "Sports", "Entertainment",
        "Health", "Science", "World News", "Crime", "Education",
        "AI & Machine Learning", "Climate & Environment", "Real Estate",
        "Automobiles", "Lifestyle & Fashion", "Food & Cooking",
        "Travel", "History & Culture", "Religion & Spirituality"
    ]
    classification = classifier(article_text, candidate_labels)
    return classification['labels'][0]  # Return the most likely category

