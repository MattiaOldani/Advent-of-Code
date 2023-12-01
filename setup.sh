#!/bin/bash

day=$2
if [[ $day == 0* ]]; then
    day=${day:1:2}
fi

curl https://adventofcode.com/$1/day/$day/input --cookie session=$AOC --output Template/input.txt
cp -r Template $1/Day-$2

cat /dev/null > Template/input.txt

code .
clear

exit
