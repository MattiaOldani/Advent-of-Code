#!/bin/bash

day=$2
if [[ $day == 0* ]]; then
    day=${day:1:2}
fi

curl https://adventofcode.com/$1/day/$day/input --cookie session=$AOC --output template/input.txt

mkdir -p $1/Day-$2
cp template/* $1/Day-$2

cat /dev/null > template/input.txt

code .

exit
