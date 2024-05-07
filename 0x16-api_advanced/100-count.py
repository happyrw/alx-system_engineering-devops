#!/usr/bin/python3
"""
Recursively queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords
"""
import requests

def count_words(subreddit, word_list, after=None, count_dict={}):
    """
    Recursively queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    headers = {'User-Agent': 'MyBot/0.0.1'}
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if posts:
            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    if word.lower() in title.split():
                        count_dict[word.lower()] = count_dict.get(word.lower(), 0) + 1
            after = data['data']['after']
            if after:
                count_words(subreddit, word_list, after, count_dict)
            else:
                sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    print("{}: {}".format(word, count))
        else:
            print("None")
    else:
        print("None")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])

