#!/bin/bash

dir="$(pwd)/$1"
echo $dir

if [ $# -eq 0 ]
then
    echo "Nothing to find";
    exit 1;
fi

if [ ! -d $dir ]
then
    echo "Directory not found"
    exit 1;
fi

n=$(find $dir -type f | wc -l)
echo "There are $n files in $dir"