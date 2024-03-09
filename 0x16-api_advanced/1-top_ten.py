#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """
    Function to get name of top-ten hot topics
    """
    if subreddit is None:
        return 0

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    resp = requests.get(url, headers=headers, allow_redirects=False)
    # resp = requests.get(url)

    if resp.status_code == 200:
        body = resp.json()
        for i in range(10):
            title = body["data"]["children"][i]["data"]["title"]
            print(f"{title}")
    else:
        print('None')
