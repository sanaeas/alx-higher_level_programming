#!/bin/bash
# Send a GET request to the URL with a header variable X-School-User-Id
curl -sH "X-School-User-Id: 98" "$1"
