#!/usr/bin/python3
'''
    this module contains the function number_of_subscribers
'''
import requests

headers = {"User-Agent": "MyCustomUserAgent/1.0"}


def number_of_subscribers(subreddit):
    """method doc"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    if subreddit is None or type(subreddit) is not str:
        return 0
    response = requests.get(url, headers=headers).json()
    subscriptions = response.get("data", {}).get("subscribers", 0)
    return subscriptions
