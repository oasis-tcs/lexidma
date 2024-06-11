#!/usr/bin/python3
import json, glob, sys
from jsonschema import validate
schema = json.load(open(sys.argv[1]))
validate(json.load(sys.stdin), schema)
