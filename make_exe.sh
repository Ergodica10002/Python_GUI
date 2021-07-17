#!/bin/bash
# Program:
#       This program turns python script to executable file by pyinstaller
# Created: 2021/07/17
# Modified: 2021/07/17
# Author: Gary Chen (https://github.com/Ergodica10002)
if [ "$#" -lt 1 ]
then
	echo "$#"
	echo "Usage: ./make_exe.sh file.py"
	exit 1
fi

if [ "$1" == "clean" ]
then
	rm -rf build/ dist/
	rm *.spec
	exit 0
fi

pyinstaller -F -w $1
exit 0