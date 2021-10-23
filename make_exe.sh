#!/bin/bash
# Program:
#       This program turns python script to executable file by pyinstaller
# Created: 2021/07/17
# Modified: 2021/10/23
# Author: Gary Chen (https://github.com/Ergodica10002)

if [ "$#" -lt 1 ]
then
	echo "Error! No Arguments"
	echo "Usage: ./make_exe.sh file.py"
	exit 1
fi

if [ "$1" == "clean" ]
then
	if [ "$#" -lt 2 ]
	then
		echo "Clean current directory"
		rm -rf build/ dist/
		rm *.spec
	elif [ -d "$2" ]
	then
		echo "Clean $2"
		rm -rf "$2"/build/ "$2"/dist/
		rm "$2"/*.spec
	fi
	exit 0
fi

if [[ $1 == *.spec ]]
then
	pyinstaller $1
elif [[ $1 == *.py ]]
then
	pyinstaller -F -w $1
else
	echo "Error: file must be in form of *.py or *spec"
	exit 2
fi