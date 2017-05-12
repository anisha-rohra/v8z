#!/bin/bash

njsc -E -qmakedep $1 > temp.c
python ebcdic2ascii.py -H *.u $1 $2
njsc $1
