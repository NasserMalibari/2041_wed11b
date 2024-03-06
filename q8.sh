#!/bin/dash

mlalias cs2041.wed13-strings |
sed -E -n '/^\s*Addresses/,/^\s*Owners/p' | 
head -n -1 | tail -n +2 | sed -E 's/^\s*//g' | 
grep -E '^z[0-9]{7}' | sed -E 's/@.*//' | head -n 4 |
while read zid
do
    acc $zid |
    sed -E -n '/^\s*User classes/,/^\s*Misc classes/p' | 
    head -n -1 |tr ',' '\n' | 
    sed -E 's/^\s*//g' | 
    sed -E 's/^[^A-Z]*//g' | 
    grep -E '^[A-Z]{4}[0-9]{4}' | sed -E 's/t[0-3].*//' 
done |

sort | uniq -c | sed -E 's/^\s*//' | sort -nr
