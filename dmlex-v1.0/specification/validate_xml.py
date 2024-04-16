#!/usr/bin/python3
import xmlschema
import glob
schema = xmlschema.XMLSchema11('dmlex.xsd')
for file in glob.glob("*.xml"):
  print(file)
  schema.validate(file)

