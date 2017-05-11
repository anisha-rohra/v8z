#!/bin/bash

for d in $(find *temp*)
do
  rm $d
done

for d in $(find *.u)
do
  rm $d
done

for d in $(find *\_after*)
do
  rm $d
done

for d in $(find *.o)
do
  rm $d
done

rm a.out
