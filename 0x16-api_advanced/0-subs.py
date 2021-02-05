#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import json
from requests import get


def number_of_subscribers(subreddit):
    """return the number od subcribers"""
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)
    res = get(url, headers={'User-agent': 'Mozilla'}, allow_redirects=False)
    data = res.json()

    try:
        chil = data.get('data').get("children")
        subs_count = chil[0].get("data").get("subreddit_subscribers")
    except Exception:
        return 0
    return subs_count
