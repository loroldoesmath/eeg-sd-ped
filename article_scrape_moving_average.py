# Concept: 
# Fetch articles in 100-sample batches
# Compute technique mention percentages for each batch
# Calculate a moving average for the percentage of seizure-related abstracts mentioning each technique, updated after each batch

import requests
import time
import pandas as pd

# Define search function to fetch articles in batches
def fetch_articles(query, batch_size=100, total_articles=13000):
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        'query': query,
        'fields': 'title,abstract,year,paperId',
        'offset': 0,
        'limit': batch_size
    }

    all_articles = []
    seen_ids = set()  # Track article IDs to avoid duplicates

    while len(all_articles) < total_articles:
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()

            data = response.json()
            current_batch = data.get('data', [])
            new_articles = [article for article in current_batch if article['paperId'] not in seen_ids]

            all_articles.extend(new_articles)
            seen_ids.update(article['paperId'] for article in new_articles)

            if len(current_batch) < batch_size:
                break  # Stop if fewer than batch_size articles returned
            
            params['offset'] += batch_size
            time.sleep(1)  # Delay between requests for rate limiting
        
        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:
                print("Rate limit hit. Retrying after 30 seconds...")
                time.sleep(30)
            else:
                print(f"Error fetching articles: {e}")
                break

    return all_articles[:total_articles]

# Define keyword search terms
techniques = [
    'Support Vector Machine', 'neural network', 'k-nearest neighbor', 'naive bayes', 
    'linear discriminant analysis', 'linear regression'
]

def analyze_batch(articles, techniques):
    technique_counts = {tech: 0 for tech in techniques}
    technique_counts['Total Seizure Articles'] = len(articles)

    for article in articles:
        title = article.get('title', '').lower()
        abstract = article.get('abstract', '').lower() if article.get('abstract') else ""
        
        for tech in techniques:
            if tech.lower() in title or tech.lower() in abstract:
                technique_counts[tech] += 1

    return technique_counts

def compute_moving_average(results, window_size=10):
    averages = []
    for i in range(len(results)):
        window = results[max(0, i - window_size + 1):i + 1]
        avg_counts = {tech: sum(batch[tech] for batch in window) / len(window) for tech in window[0]}
        averages.append(avg_counts)
    return averages

def main():
    query = '("machine learning" AND "seizure")'
    batch_size = 100
    total_articles = 13000
    window_size = 10  # Moving average window size
    
    all_articles = fetch_articles(query, batch_size, total_articles)
    results = []

    for i in range(0, len(all_articles), batch_size):
        batch = all_articles[i:i + batch_size]
        batch_result = analyze_batch(batch, techniques)
        results.append(batch_result)

    moving_averages = compute_moving_average(results, window_size)

    # Display final moving averages
    for i, avg in enumerate(moving_averages, start=1):
        print(f"Moving average for batch {i}: {avg}")

if __name__ == "__main__":
    main()
