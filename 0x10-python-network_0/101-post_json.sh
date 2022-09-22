#!/bin/bash
# curl a JSON file
curl -s -X POST "$1" -d @"$2" --header "Content-Type: application/json"
