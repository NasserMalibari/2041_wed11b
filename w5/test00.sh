#!/bin/dash

#######################
#
# Testing behaviour of adding a removed file
# for COMP2041/9044 assignment.
# Author: Nasser Malibari
#
#######################


trap 'rm "$exp" "$actual" -rf "$temp_dir"' INT HUP QUIT TERM EXIT


temp_dir=$(mktemp -d)

PATH=${PATH}:$(pwd)

cd $temp_dir

exp=$(mktemp)
actual=$(mktemp)

pushy-init 2>&1 $actual

cat > "$exp" <<HERE
Initialized empty pushy repository in .pushy
HERE

if ! diff "$actual" "$exp" > /dev/null
then
	echo "failed test!"
	exit 1	
fi


echo "abc" > a
pushy-add a 2>&1 $actual
cat > "$exp" <<HERE
HERE


if ! diff "$actual" "$exp" > /dev/null
then
	echo "failed test!"
	exit 1	
fi


pushy-commit -m "commit 1" 2>&1 $actual

cat > "$exp" <<HERE
Committed as commit 0
HERE


if ! diff "$actual" "$exp" > /dev/null
then
	echo "failed test!"
	exit 1	
fi

rm a
pushy-add a 2>&1 $actual

cat > "$exp" <<HERE
HERE


if ! diff "$actual" "$exp" > /dev/null
then
	echo "failed test!"
	exit 1	
fi

pushy-commit -m "removed file a" 2>&1 $actual

cat > "$exp" <<HERE
Committed as commit 1
HERE


if ! diff "$actual" "$exp" > /dev/null
then
	echo "failed test!"
	exit 1	
fi


