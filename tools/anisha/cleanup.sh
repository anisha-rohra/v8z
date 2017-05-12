#!/bin/bash

for d in $(find $1/*temp*)
do
  rm $d
done

for d in $(find $1/*.u)
do
  rm $d
done

for d in $(find $1/*\_after*)
do
  rm $d
done

for d in $(find $1/*.o)
do
  rm $d
done

rm $1/a.out
