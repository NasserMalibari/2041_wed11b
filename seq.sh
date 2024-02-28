#!/bin/sh


# if num args = 1

# check first argument is a number



if [ "$#" -eq 1 ]
then
    start=1
    increment=1
    end="$1"
fi

if [ "$#" -eq 2 ] 
then
    start="$1"
    increment=1
    end="$2"
fi


if [ "$end" -eq "$end"  ] 2> /dev/null
then
    echo "all good"
else 
    echo "not a number"
    exit 1
fi
# if num args = 2





current=$start


# while test $current -le $end
while [ $current -le $end ]
do 

    echo "$current"
    current=$(( current + increment  ))

done
# while current <= end

    # print current
    # increment 
