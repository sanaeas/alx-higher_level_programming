#!/usr/bin/python3
"""
Use the GitHub API to display your id
"""

if __name__ == '__main__':
    import sys
    import requests

    username = sys.argv[1]
    password = sys.argv[2]

    r = requests.get('https://api.github.com/user',
                     auth=(username, password))
    print(r.json().get('id'))
