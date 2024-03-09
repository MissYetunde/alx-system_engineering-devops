#!/usr/bin/python3
"""
a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""

import requests
import sys


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursive function to get titles of all hot articles for a subreddit
    """

    # Initialize the hot_list if not provided
    if hot_list is None:
        hot_list = []

    # Base case: subreddit is not valid
    if subreddit is None:
        return None

    # Construct the URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set parameters for pagination
    params = {'limit': 100, 'after': after}

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    # Make the request to the Reddit API
    response = requests.get(url, params=params,
                            headers=headers, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract titles and add them to the hot_list
        posts = data.get('data', {}).get('children', [])
        titles = [post['data']['title'] for post in posts]
        hot_list.extend(titles)

        # Check if there are more pages to retrieve
        after = data.get('data', {}).get('after')
        if after is not None:
            # Recursive call with the updated after parameter
            return recurse(subreddit, hot_list, after)

        else:
            # Base case: no more pages, return the hot_list
            return hot_list
    else:
        # Base case: invalid subreddit or other error
        return None
