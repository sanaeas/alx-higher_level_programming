#!/bin/bash
# Takes in a URL, and displays the size of the body of the response
curl -Is "$1" | grep -i 'Content-Length' | awk '{print $2}'
