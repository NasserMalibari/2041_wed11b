#!/bin/sh

for file in *.c # for file in a.c b.c wc.c uniq.c
do 
    echo "$file includes:"
    grep -E '^#include' "$file" | # grab all #include lines
    sed -E 's/^#include\s*[<"]/\t/' | # remove the #include and first (" | <) and replace with tab
    sed -E 's/[>"].*//' | # remove the last (> | ")
    # tr .... |

done
