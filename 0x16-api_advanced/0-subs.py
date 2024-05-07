#!/usr/bin/python3
"""Write a function that queries the Reddit API and
returns the number of subscribers (not active users,
total subscribers) for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """reddit API"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, allow_redirects=False)
    if res.status_code == 200:
        results = res.json().get("data")
        return results.get("subscribers")
    else:
        return 0
