#!/bin/bash

check_file () {
    if [ -f "$1" ]
    then
        echo "$1 found"
    else
        echo "$1 not found"
        exit -1
    fi
}

echo "Checking for all files"

check_file "apiary.apib"
check_file "README.md"
