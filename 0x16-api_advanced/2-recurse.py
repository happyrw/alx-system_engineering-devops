#!/usr/bin/python3
"""
Recursively queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit
"""
import requests

def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    headers = {'User-Agent': 'MyBot/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if posts:
            for post in posts:
                hot_list.append(post['data']['title'])
            after = data['data']['after']
            if after:
                recurse(subreddit, hot_list)
            else:
                return hot_list
        else:
            return None
    else:
        return None

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")

