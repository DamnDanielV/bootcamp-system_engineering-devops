#!/usr/bin/python3
"""uaing refcursions to get a data"""
from requests import get


def count_words(subreddit, word_list, after={}, count={}):
    """ rcursion function to get keywords"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = get(url, headers={"User-agent": "Mozilla"}, params={"after": after},
              allow_redirects=False)

    if after is None:
        return count

    try:
        data = res.json()
        child = data['data']['children']
        for ch in child:
            for word in ch['data']['title'].split():
                for keyword in word_list:
                    if keyword not in count.keys():
                        count[keyword] = 0
                    if word.upper() == keyword.upper():
                        count[keyword] += 1

        after_copy = data['data']['after']
        count = count_words(subreddit, word_list, after_copy, count)

        if after == {}:
            for key in [v[0] for v in sorted(count.items(),
                        key=lambda keyword: (-keyword[1], keyword[0]))]:
                if count[key] > 0:
                    print("{}: {}".format(key, count[key]))

        return count

    except Exception:
        return None
