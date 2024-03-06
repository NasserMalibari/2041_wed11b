#!/bin/dash

if [ "$#" -ne 1 ]
then
    echo "Usage: ./is_prime <number>" 
    exit 2
fi

num=$1
i=2
# i < sqrt(n)
# i*i < n
while [ $(( i * i )) -le "$num"  ]
do
    rem=$((num % i))

    if [ $rem -eq 0 ]
    then
        echo "$i is a factor :("
        echo "$num is not prime"
        exit 2
    fi

    i=$((i+1))
done


echo "$num is prime"
exit 0