#!/bin/sh

for file in *.c # for file in a.c b.c wc.c uniq.c
do 
    echo "$file includes:"
    grep -E "^\s*#include" $file |
    sed .... |
    tr .... |
    
done
