#!/usr/bin/python3
"""first 10 hot posts listed for a given subreddit"""
import json
from requests import get


def top_ten(subreddit):
    """top ten post"""
    # post = []
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)
    res = get(url, headers={'User-agent': 'Mozilla'}, allow_redirects=False)
    data = res.json()
    try:
        children = data.get("data").get("children")
        # print("longuitud")
        # print(len(children))
        for i in range(10):
            print(children[i].get("data").get("title"))
            # post.append(children[i].get("data").get("title"))
        # print (post)
    except Exception:
        print(None)
