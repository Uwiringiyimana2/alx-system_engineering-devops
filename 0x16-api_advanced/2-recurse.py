#!/usr/bin/python3
"""recursive function that queries the Reddit API """
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """def recurse(subreddit, hot_list=[])"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by eric)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    try:
        data = response.json()
        if 'data' not in data or 'children' not in data['data']:
            print("Error: Unexpected response format")
            return None
        results = data['data']
        after = results.get("after")
        count += results.get("dist")
        for child in results.get("children"):
            title = child.get("data").get("title")
            hot_list.append(title)

        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        return hot_list
    except Exception as e:
        print(f"Error: {e}")
        return None
