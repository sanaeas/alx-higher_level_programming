#!/usr/bin/python3
"""
Send a request to the URL and display the body of the response
Manage urllib.error.HTTPError exceptions
"""

if __name__ == '__main__':
    import sys
    import urllib.error
    import urllib.request

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            res_body = response.read()
            print(res_body.decode('UTF-8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
