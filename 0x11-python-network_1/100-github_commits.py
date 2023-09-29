#!/usr/bin/python3
"""
List 10 commits from a repo
"""

if __name__ == '__main__':
    import sys
    import requests

    repo = sys.argv[1]
    owner = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)

    r = requests.get(url)
    commits = r.json()
    for i in range(10):
        print('{}: {}'.format(
              commits[i]['sha'],
              commits[i]['commit']['author']['name']))
