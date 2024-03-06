# Run in dmlex-v1.0/specification/serializations/RDF/

for f in `ls ../../examples/examples/source/*.rdf`
do
    echo "Validating $f"
    pyshacl -s ontology/dmlex.shacl -df turtle $f -e ontology/dmlex.ttl -i rdfs
done
