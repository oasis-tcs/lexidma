#!/usr/bin/python3
import xmlschema, glob, sys
xmlschema.XMLSchema11(sys.argv[1]).validate(sys.stdin.read())
