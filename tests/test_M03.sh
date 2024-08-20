#!/bin/bash

# Run M03Basics01.sh
# This file assumes you are running from the root directory of the repository

bash M03Basics01.sh

# Check if the file was downloaded and renamed correctly
if [ -f "msse_gist.txt" ]; then
    echo "Test Passed: File 'msse_gist.txt' exists in the parent directory."
else
    echo "Test Failed: File 'msse_gist.txt' does not exist in the parent directory."
    exit 1
fi