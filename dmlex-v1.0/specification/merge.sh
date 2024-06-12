#!/bin/sh
java -cp "lib/merger.jar:lib/resolver.jar:lib/xercesImpl.jar:lib/xml-apis.jar" Merger dmlex.xml $1
