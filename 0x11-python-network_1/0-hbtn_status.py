#!/usr/bin/python3
"""A script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == '__main__':
    import urllib.request
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        body_res = res.read()
        print('Body response:')
        print('\t- type:', type(body_res))
        print('\t- content:', body_res)
        print('\t- utf8 content:', body_res.decode('utf-8'))
