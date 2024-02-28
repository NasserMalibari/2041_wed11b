#!/bin/sh

if [ "$#" -eq 1 ]
then
    start=1
    increment=1
    end="$1"

elif [ "$#" -eq 2 ] 
then
    start="$1"
    increment=1
    end="$2"
elif [ "$#" -eq 3 ] 
then
    start="$1"
    increment="$2"
    end="$3"
fi


if [ "$end" -eq "$end"  ] 2> /dev/null
then
    :
else 
    echo "not a number"
    exit 1
fi

if [ "$increment" -eq "$increment"  ] 2> /dev/null
then
    :
else 
    echo "not a number"
    exit 1
fi

if [ "$start" -eq "$start"  ] 2> /dev/null
then
    :
else 
    echo "not a number"
    exit 1
fi

if [ "$end" -eq "$end"  ] 2> /dev/null
then
    :
else 
    echo "not a number"
    exit 1
fi

if [ "$increment" -eq "$increment"  ] 2> /dev/null
then
    :
else 
    echo "not a number"
    exit 1
fi


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
