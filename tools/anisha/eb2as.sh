#!/bin/sh

CFLAG=0
for var in $@
do
    if [ $(echo $var | sed -E 's/.+(\.cpp)/\1/') != $var ]
    then
        break
    fi

    if [ $(echo "$var" | sed -E 's/.+(\.c)/\1/') != $var ] || [ $(echo "$var" | sed -E 's/.+(\.cc)/\1/' != $var) ]
    then
        CFLAG=1
        break
    fi
done

if [ $CFLAG = 0 ]
then
    xlclang++ -E -qmakedep $@ > garbage.c
else
    xlclang -E -qmakedep $@ > garbage.c
fi

count=0
for var in $@
do
    if [ $(echo "$var" | sed -E 's/.+(\.c)/\1/') != "$var" ] || [ $(echo "$var" | sed -E 's/.+(\.cc)/\1/') != "$var" ] || [ $(echo "$var" | sed -E 's/.+(\.cpp)/\1/') != "$var" ]
    then
        HEADER=$(echo $var | sed -E 's/.*\/([a-z0-9_]+)\.[a-z]+/\1.u/')
        TEMP=$(echo $var | sed -E 's/(.+)\.([a-z]+)/\1_temp.\2/')
        python ebcdic2ascii.py -H $HEADER $var $TEMP
        COMPILE[count]=$TEMP
        (( count++ ))
    else
        COMPILE[count]=$var
        (( count++ ))
    fi
done

if [ $CFLAG = 1 ]
then
    xlclang ${COMPILE[*]}
else
    xlclang++ ${COMPILE[*]}
fi

./cleanup.sh .
