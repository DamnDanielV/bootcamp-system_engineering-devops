#!/usr/bin/python3
"""recursive way"""
import json
from requests import get


def recurse(subreddit, after={}):
    """recursive way function"""
    lists = []
    url = "https://www.reddit.com/r/{}.json".format(subreddit)
    res = get(url, headers={"User-agent": "Mozilla"}, params={"after": after},
              allow_redirects=False)
    if after is None:
        return lists
    try:
        data = res.json()
        children = data['data']['children']
        for ch in children:
            lists.append(ch['data']['title'])
        after = data['data']['after']

        rec = recurse(subreddit, after)
        if lists:
            rec.extend(lists)
        return rec

    except Exception:
        return None
