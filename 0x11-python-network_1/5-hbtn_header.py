#!/usr/bin/python3
"""Display the value of the variable X-Request-Id in the response header"""

if __name__ == '__main__':
    import sys
    import requests

    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])
