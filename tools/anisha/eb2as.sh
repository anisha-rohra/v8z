#!/bin/bash

njsc -E -qmakedep test.c > test_temp.c
python ebcdic2ascii.py -H test.u test.c test_after.c
njsc test.c
