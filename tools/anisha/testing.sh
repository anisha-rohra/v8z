#!/bin/sh
njsc -E -qmakedep $@ > garbage.c

filecount=0
flagcount=0
for var in $@
do
    if [ $(echo "$var" | sed -E 's/.+(.c)/\1/') != "$var" ] || [ $(echo "$var" | sed -E 's/.+(.cc)/\1/') != "$var" ] || [ $(echo "$var" | sed -E 's/.+(.cpp)/\1/') != "$var" ]
    then
        HEADER=$(echo $var | sed -E 's/.*\/([a-z_]+).[a-z_]+/\1.u/')
        TEMP=$(echo $var | sed -E 's/(.+).([a-z_]+)/\1_temp.\2/')
        echo $HEADER
        echo $TEMP
        python ebcdic2ascii.py -H $HEADER $var $TEMP
        FILES[filecount]=$TEMP
        (( filecount++ ))
    else
        FLAGS[flagcount]=$var
        (( flagcount++ ))
    fi
done

njsc ${FLAGS[*]} ${FILES[*]}
