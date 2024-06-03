import rdflib
from collections import defaultdict
from rdflib.namespace import RDF, RDFS, OWL, URIRef
from rdflib.collection import Collection

DMLEX = "https://docs.oasis-open.org/lexidma/dmlex/v1.0/schemas/RDF/dmlex.ttl#"
DMLEX_SHACL = "https://docs.oasis-open.org/lexidma/dmlex/v1.0/schemas/RDF/dmlex.shacl#"

def parse_rdf():
    g = rdflib.Graph()
    g.parse("ontology/dmlex.ttl", format="turtle")

    props = defaultdict(list)
    for s, p, o in g.triples((None, RDFS.domain, None)):
        if isinstance(o, rdflib.term.URIRef):
            if str(o).startswith(DMLEX + "Has"):
                for domain_class in g.subjects(RDFS.subClassOf, o):
                    props[domain_class].append(s)
            else:
                props[o].append(s)
        else:
            for listname in g.objects(o, OWL.unionOf):
                for item in Collection(g, listname):
                    props[item].append(s)

    ranges = defaultdict(list)
    for s, p, o in g.triples((None, RDFS.range, None)):
        if isinstance(o, rdflib.term.URIRef):
            ranges[s].append(o)

    with open("ontology/dmlex.shacl", "w") as file:
        file.write("# This file was generated from dmlex.ttl by " + 
            "gen_shacl_from_rdf.py\n")
        file.write("@prefix sh: <http://www.w3.org/ns/shacl#> .\n")
        file.write(f"@prefix dmlex: <{DMLEX}> .\n")
        file.write(f"@prefix : <{DMLEX_SHACL}> .\n\n")
        for class_uri in g.subjects(RDF.type, OWL.Class):
            if (isinstance(class_uri, rdflib.term.URIRef) and 
                not str(class_uri).startswith(DMLEX + "Has")):
                uri = str(class_uri)
                name = uri.split("#")[-1]

                subclasses = []
                restrictions = defaultdict(lambda: defaultdict(lambda: [0,-1]))
                for o in g.objects(class_uri, RDFS.subClassOf):
                    if (isinstance(o, rdflib.term.URIRef) and
                        not str(o).startswith(DMLEX + "Has")):
                        subclasses.append(str(o))
                    elif isinstance(o, rdflib.term.BNode):
                        for o2 in g.objects(o, OWL.onProperty):
                            for o3 in g.objects(o, OWL.cardinality):
                                restrictions[class_uri][o2] = [o3, o3]
                            for o3 in g.objects(o, OWL.maxCardinality):
                                restrictions[class_uri][o2] = [0, o3]
                            for o3 in g.objects(o, OWL.minCardinality):
                                restrictions[class_uri][o2] = [o3, -1]
                file.write(f"""
:{name}Shape ;
    a sh:NodeShape ;
    sh:targetClass dmlex:{name} ;
    sh:closed false""")
                for prop in props[class_uri]:
                    file.write(f""" ;
    sh:property [
      sh:path dmlex:{prop.split("#")[-1]} """)
                    if prop in restrictions[class_uri]:
                        min_card, max_card = restrictions[class_uri][prop]
                        if min_card >= 0:
                            file.write(f""" ;
      sh:minCount {min_card}""")
                        if max_card >= 0:
                            file.write(f""" ;
      sh:maxCount {max_card}""")
                    for range in ranges[prop]:
                        if range.startswith(DMLEX):
                            file.write(f""" ;
      sh:class dmlex:{range.split("#")[-1]} """)
                    file.write(" ]")
                    
                file.write("  .\n\n")





if __name__ == "__main__":
    parse_rdf()
