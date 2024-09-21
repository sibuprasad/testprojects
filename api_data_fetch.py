"""
Fetch NDTV news vlogs sports news data
"""

import requests

# Replace 'your_api_key_here' with your actual NewsAPI key
API_KEY = 'de37af6fc7694959a9de9c3734fd1561'
BASE_URL = 'https://newsapi.org/v2/top-headlines'

# Parameters for the API request
params = {
    'apiKey': API_KEY,
    'category': 'sports',
    'country': 'in'  # 'in' is the country code for India
}

# Making the API request
response = requests.get(BASE_URL, params=params)

# Checking if the request was successful
if response.status_code == 200:
    data = response.json()
    articles = data.get('articles', [])

    # Print the title and description of each article
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}")
        print("-" * 80)
else:
    print(f"Failed to fetch news: {response.status_code}")
    print(f"Response: {response.json()}")
