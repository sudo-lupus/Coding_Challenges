#!/bin/bash
# Bash Basics - Check for File Existence

if [ $# -eq 0 ]
then
    echo "Nothing to find";
    exit 0;
fi

if ls | grep -q $1
then
    echo "Found $1";
    exit 1;
else
    echo "Can't find $1"
    exit 0;
fi