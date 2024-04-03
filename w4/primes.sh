#!/bin/dash

# print the prime numbers less than the specified argument

if [ $# -ne 1 ] ||  ! [ "$1" -eq "$1" ] 2> /dev/null || [ "$1" -lt 0 ]; then
    echo "Usage: $0 <number>"
    exit 2
fi

limit=$1
p=2

while [ "$p" -lt "$limit" ]; do
  if ./is_prime.sh "$p" > /dev/null; then
    echo $p
  fi
  p=$((p + 1))
done







echo "$img" | grep -E "..." 

exit_stat="$?"