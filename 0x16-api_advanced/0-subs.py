#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers for a given subreddit
"""
import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'MyBot/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subscribers = number_of_subscribers(sys.argv[1])
        print(subscribers)

