#!/usr/bin/python3
"""
Send a request to the URL and displays the body of the response
If the HTTP status code is >= 400, print: Error code: {status_code}
"""

if __name__ == '__main__':
    import sys
    import requests

    r = requests.get(sys.argv[1])
    if (r.status_code >= 400):
        print('Error code:', r.status_code)
    else:
        print(r.text)
