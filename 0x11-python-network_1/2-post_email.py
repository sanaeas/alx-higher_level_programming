#!/usr/bin/python3
"""
Send a POST request to a URL with the email as a parameter,
and display the body of the response (decoded in utf-8)
"""

if __name__ == '__main__':
    import sys
    import urllib.parse
    import urllib.request

    value = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
