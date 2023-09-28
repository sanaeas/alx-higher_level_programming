#!/bin/bash
# Take in a URL and display all HTTP methods the server will accept
curl -sI "$1" | grep -i "Allow" | cut -d " " -f 2-