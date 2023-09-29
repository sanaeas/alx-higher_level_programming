#!/usr/bin/python3
"""Send a POST request to the URL with the email as a parameter"""

if __name__ == '__main__':
    import sys
    import requests

    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
