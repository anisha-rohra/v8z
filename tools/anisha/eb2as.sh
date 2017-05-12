#!/bin/sh

njsc -E -qmakedep $1 > garbage.c
HEADER=$(echo $1 | sed -E 's/.*\/([a-z]+).[a-z]+/\1.u/')
TEMP=$(echo $1 | sed -E 's/(.+).([a-z]+)/\1_temp.\2/')
python ebcdic2ascii.py -H $HEADER $1 $TEMP
njsc $TEMP
