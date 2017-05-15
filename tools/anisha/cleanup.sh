#!/bin/bash

for d in $(find $1 -name "*_temp.*")
do
  rm $d
done

for d in $(find $1 -name "*.u")
do
  rm $d
done

for d in $(find $1 -name "*_after.*")
do
  rm $d
done

for d in $(find $1 -name "*.o")
do
  rm $d
done

if [ -f $1/garbage.c ]
then
    rm $1/garbage.c
fi

if [ -f $1/a.out ]
then
    rm $1/a.out
fi
