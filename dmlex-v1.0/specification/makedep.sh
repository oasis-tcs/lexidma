#!/bin/sh
DEPS=`xmlstarlet sel -T -t -m //xi:include/@href -v . -n dmlex.xml`
OLDDEPS=$DEPS
while true; do
	NEWDEPS=
	for DEP in $OLDDEPS; do
		INCLUDES=`xmlstarlet sel -T -t -m //xi:include/@href -v . -n $DEP`
		for INCL in $INCLUDES; do
			NEWDEPS="$NEWDEPS `dirname $DEP`/$INCL"
		done
	done
	[ -z "$NEWDEPS" ] && break;
	DEPS="$DEPS $NEWDEPS"
	OLDDEPS="$NEWDEPS"
done
echo $DEPS
