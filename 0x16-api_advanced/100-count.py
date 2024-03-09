#!/usr/bin/python3
"""
a recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords
""" 
import requests

def count_words(subreddit, word_list, after='', counter=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive).
    """
    # Base URL for Reddit API
    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"

    # Add 'after' parameter for pagination
    if after:
        base_url += f"&after={after}"

    # Initialize counter dict on first call
    if counter is None:
        counter = {word.lower(): 0 for word in word_list}

    # Headers for Reddit API request
    headers = {'User-agent': 'Keyword counter bot 0.1'}

    # Make the request to Reddit API
    response = requests.get(base_url, headers=headers)

    # Check for a valid response
    if response.status_code != 200:
        return

    # Convert response to JSON
    data = response.json()

    # Extract articles and next page's 'after' token
    articles = data.get('data', {}).get('children', [])
    after = data.get('data', {}).get('after', '')

    # Process titles in the articles
    for article in articles:
        title = article.get('data', {}).get('title', '').lower()
        for word in counter.keys():
            counter[word] += title.split().count(word)

    # If 'after' is not None, continue recursion, else print results
    if after:
        count_words(subreddit, word_list, after, counter)
    else:
        # Sort the results
        sorted_results = sorted(
            [(k, v) for k, v in counter.items() if v > 0],
            key=lambda x: (-x[1], x[0])
        )

        # Print the results
        for word, count in sorted_results:
            print(f"{word}: {count}")

