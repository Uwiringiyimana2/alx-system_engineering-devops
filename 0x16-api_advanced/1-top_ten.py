#!/usr/bin/python3
"""
function that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """queries the Reddit API and prints the
    titles of the first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by eric)"
    }
    params = {
        "limit": 10
    }
    res = requests.get(url, params=params,
                       headers=headers, allow_redirects=False)
    if res.status_code == 200:
        results = res.json().get("data")
        [print(c.get("data").get("title")) for c in results.get("children")]
    else:
        print("None")
