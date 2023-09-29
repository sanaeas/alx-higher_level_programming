#!/usr/bin/python3
"""
Take a URL, and display the value of the X-Request-Id
variable found in the header of the response
"""

if __name__ == '__main__':
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as response:
        req_id = response.getheader('X-Request-Id')
        print(req_id)
