#!/bin/sh

export PATH=/home/barboza/temp/bin/:$PATH
export PATH=/usr/lpp/ported/bin/:$PATH
export PATH=/sysroot/usr/lpp/OpenSource/bin/:$PATH
export PYTHONDIR="/home/barboza/python-2.7.6"
export PATH=$PYTHONDIR/bin:$PATH
alias make=/home/barboza/buildtools/bin/make
export PATH=/gsa/tlbgsa/projects/x/xlcmpbld/run/vacpp/dev/os390/zosv2c1/D170222/:$PATH
export CC="xlclang"
export CXX="xlclang++"
export LINK="xlclang++"
export GYP_DEFINES="OS=os390 gyp_parallel_support=False"
export CFLAGS="-q64  -Wno-unknown-escape-sequence "
export CXXFLAGS="-q64  -Wno-unknown-escape-sequence "
export LDFLAGS="-q64 "
export STEPLIB=TSCTEST.CEEZ230.SCEERUN2:$STEPLIB
