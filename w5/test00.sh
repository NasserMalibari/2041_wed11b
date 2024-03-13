#!/bin/dash


temp_dir=$(mktemp -d)

PATH=${PATH}:$(pwd)

cd $temp_dir

exp=$(mktemp)
actual=$(mktemp)

pushy-init 2>&1 $actual

cat > "$exp" <<HERE
"Initialised repository in .pushy"
HERE

if ! diff "$actual" "$exp" 2>&1 /dev/null
then
	echo "failed test!"
	exit 1	
fi


echo "abc" > a
pushy-add a 2>&1 $actual
pushy-commit -m "commit 1" 2>&1 $actual

rm a
pushy-add a 2>&1 $actual
pushy-commit -m "removed file a" 2>&1 $actual

rm -rdf .pushy



