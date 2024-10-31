#!/bin/bash

ng () {
	echo "${1} is kasu"
	res=1
}

res=0
a=yamada

[ "$a" = ueada ] || ng "$LINENO"
[ "$a" = yamada ] || ng "$LINENO"

exit $res

