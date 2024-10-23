import requests
import time
import pandas as pd

# Define your search function to fetch articles
def fetch_articles(query):
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        'query': query,
        'offset': 0,
        'limit': 100  # Fetch in batches of 100
    }
    
    articles = []
    
    while len(articles) < 500:  # Stop when we have 500 articles
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            
            data = response.json()
            articles.extend(data.get('data', []))  # Safely get 'data'
            
            # Debug: Print the number of articles fetched in this batch
            print(f"Fetched {len(data.get('data', []))} articles.")
            
            # Break if there are no more results or if we've reached 500 articles
            if len(data['data']) < params['limit'] or len(articles) >= 500:
                break
            
            params['offset'] += params['limit']
            time.sleep(1)  # Delay between requests to avoid rate limits
        
        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:
                print("Rate limit hit. Retrying after 30 seconds...")
                time.sleep(30)  # Wait for 30 seconds before retrying
            else:
                print(f"Error fetching articles: {e}")
                return []
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return []

    return articles

# Define your keyword search terms
techniques = [
    'Support Vector Machine', 'SVM', 'neural network', 'RNN', 'CNN', 
    'ANN', 'k-nearest neighbor', 'KNN', 'naive bayes', 'linear discriminant analysis', 
    'machine learning', 'seizure detection'
]

def analyze_articles(articles):
    technique_counts = {tech: 0 for tech in techniques}
    technique_counts['Other'] = 0  # For articles that don't mention any keywords
    chb_mit_count = 0
    total_articles = len(articles)
    article_titles = []

    # Debug: Print total articles found
    print(f"Total articles found: {total_articles}")
    
    # Count occurrences of each technique in the titles and abstracts
    for paper in articles:
        title = paper.get('title', '').lower()
        abstract = paper.get('abstract', '').lower()  # Use lowercase for case-insensitive match
        year = paper.get('year', None)  # Get the publication year

        # Filter for articles published from 2021 to 2024 with specific words in the title
        if year and 2021 <= year <= 2024 and all(word in title for word in ['machine', 'learning', 'seizure']):
            article_titles.append(title)  # Save the title
            
            # Check for CHB-MIT mentions
            if 'chb-mit' in title or 'chb-mit' in abstract:
                chb_mit_count += 1
            
            found_technique = False
            for tech in techniques:
                if tech.lower() in title or tech.lower() in abstract:
                    technique_counts[tech] += 1
                    found_technique = True
            
            # Increment 'Other' if no technique was found
            if not found_technique:
                technique_counts['Other'] += 1

    # Calculate percentages
    total_technique_articles = sum(technique_counts.values())
    technique_percentages = {tech: (count / total_technique_articles) * 100 if total_technique_articles > 0 else 0 
                             for tech, count in technique_counts.items()}
    
    chb_mit_percentage = (chb_mit_count / total_articles) * 100 if total_articles > 0 else 0

    return technique_counts, article_titles, chb_mit_percentage

def save_to_csv(article_titles):
    df = pd.DataFrame(article_titles, columns=['Article Title'])
    file_path = 'articles_2021_2024.csv'
    df.to_csv(file_path, index=False)
    print(f"Article titles saved to {file_path}")

def main():
    query = "machine learning seizure"  # Searching for these keywords in the title
    
    articles = fetch_articles(query)
    
    if articles:
        counts, titles, chb_mit_percentage = analyze_articles(articles)
        
        # Display counts for techniques
        print("Count of articles mentioning machine learning techniques:")
        for tech, count in counts.items():
            print(f"{tech}: {count}")
        
        # Display percentage of articles mentioning CHB-MIT
        print(f"Percentage of articles mentioning CHB-MIT: {chb_mit_percentage:.2f}%")
        
        # Save article titles to CSV
        save_to_csv(titles)
    else:
        print("No articles were fetched.")

if __name__ == "__main__":
    main()
