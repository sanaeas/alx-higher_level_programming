#!/bin/bash
# Send a POST request to the passed URL with email ans subject variables
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
