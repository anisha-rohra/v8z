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

rm $1/garbage.c

rm $1/a.out
