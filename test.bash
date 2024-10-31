#!/bin/bash
# SPDX-FileCopyrightText: 2024 Horiguti 
# SPDX-License-Identifier: BSD-3-Clause


ng () {
	echo "${1} is kasu"
	echo "correct value is ${2} but ./plus output is ${3}"
	res=1
}

res=0
out=$(seq 5 | ./plus)

[ "${out}" = 15 ] || ng "$LINENO" 15 $out
[ "$res" = 0 ] && echo 'OK'

exit $res

