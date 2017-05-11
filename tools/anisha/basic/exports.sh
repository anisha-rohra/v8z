#!/bin/bash

export PATH=/gsa/tlbgsa/projects/xcp/xlcmpbld/run/vacpp/dev/os390/zosv2c1/D170222/:$PATH
export PATH=/usr/lpp/ported/bin/:$PATH
export PATH=/sysroot/usr/lpp/OpenSource/bin/:$PATH

xlclang -E -qmakedep test.c add.h -I directed/ > test_temp.c
python ebcdic2ascii.py -H test.u test.c test_after.c
xlclang test.c
