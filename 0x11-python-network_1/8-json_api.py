#!/usr/bin/python3
"""
Send a POST request to http://0.0.0.0:5000/search_user
with the given letter as a parameter
"""

if __name__ == '__main__':
    import sys
    import requests

    if len(sys.argv) == 1:
        letter = ''
    else:
        letter = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': letter})
    try:
        result = r.json()
        if not result:
            print('No result')
        else:
            print('[{}] {}'.format(result.get('id'), result.get('name')))
    except ValueError:
        print('Not a valid JSON')
