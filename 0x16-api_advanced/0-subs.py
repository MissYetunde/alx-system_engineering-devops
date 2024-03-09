#!/usr/bin/python3
"""
A python script that retruns the number of (all-time)
subscribers of a subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    A function def to get the number of (all time subscribers
    of a subreddit. """
    if subreddit is None:
        return 0

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    resp = requests.get(url, headers=headers, allow_redirects=False)
    # resp = requests.get(url)
    if resp.status_code == 200:
        body = resp.json()
        subscribers = body["data"]["subscribers"]
        return subscribers
    else:
        return 0
