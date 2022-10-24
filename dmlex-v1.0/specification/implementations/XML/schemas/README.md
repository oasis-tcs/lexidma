# README

This directory contains the schemas for the XML serialization of the DMLex specification.
The schemas are written in RelaxNG and follow the modular structure of the specification, in particular:
* Each module is stored in its own file, with the filename starting with "dmlex-module". 
  Apart from the Core module, they cannot be used directly, but rather by including them in a schema.
* There are currently three schemas which include the modules and are meant for the three types of dictionaries covered: 
  dmlex-monolingual for monolingual lexical resources, 
  dmlex-bilingual for biingual lexical resources, and 
  dmlex-multilingual for multilingual lexical resources.
 * To see the encoding and to test the schemas example files (*-test.xml) are also included.
