#!/usr/bin/python3
import json
from jsonschema import validate
import glob
schema = json.load(open('dmlex.schema.json'))
for file in glob.glob("*.json"):
  if file.endswith('.schema.json'):
    continue
  print(file)
  validate(json.load(open(file)), schema)

