#!/usr/bin/python3
"""
This doc for module
"""
import requests


def recurse(subreddit, after=None):
    """method doc"""
    headers = {"User-Agent", "MyCustomUserAgent/1.0"}
    params = {"after": after}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    response = request.get(
            url,
            allow_redirect=False,
            headers=headers,
            params=params
            )
    all_posts = []
    if response.staus_code == 200:
        data = response.json()
        after = data["data"]["after"]
        if after is None:
            return all_posts
        for post in data["data"]["children"]:
            all_posts .append(post["data"]["title"])
        next = recurse(subreddit, after)
        all_posts.extend(next)
        return all_posts
    return None
