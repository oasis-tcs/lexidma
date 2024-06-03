import rdflib
from rdflib.namespace import RDF, RDFS, OWL, URIRef
from collections import defaultdict
from rdflib.collection import Collection

DMLEX = "https://docs.oasis-open.org/lexidma/dmlex/v1.0/schemas/RDF/dmlex.ttl#"

def describe_property(g, property, file, restrictions):
    file.write(f"""
    <listitem>
        <para><literal>dmlex:{property.split("#")[-1]}</literal>""")
    file.write(f"""{restrictions[property]}""")
    for o in g.objects(property, RDFS.range):
        if isinstance(o, rdflib.term.URIRef):
            if str(o).startswith(DMLEX):
                file.write(""" reference to <olink targetptr="rdf_""" +
                           f"""{str(o)[len(DMLEX):]}">{str(o)[len(DMLEX):]}</olink>""")
            else:
                file.write(f""" of type <literal>{o}</literal>""")
    for o in g.objects(property, RDFS.subPropertyOf):
        if isinstance(o, rdflib.term.URIRef):
            file.write(f""" (subproperty of <literal>{o}</literal>)""")
    file.write("""</para>
    </listitem>""")


def parse_rdf():
    g = rdflib.Graph()
    g.parse("ontology/dmlex.ttl", format="turtle")

    props = defaultdict(list)
    # First scan for domains
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

    # Generate for each class
    for class_uri in g.subjects(RDF.type, OWL.Class):
        if (isinstance(class_uri, rdflib.term.URIRef) and 
            not str(class_uri).startswith(DMLEX + "Has")):
            uri = str(class_uri)
            name = uri.split("#")[-1]

            definition = "DEFINITION MISSING"
            for o in g.objects(class_uri, RDFS.comment):
                definition = str(o)
                break

            subclasses = []
            restrictions = defaultdict(lambda: defaultdict(lambda: " OPTIONAL"))
            for o in g.objects(class_uri, RDFS.subClassOf):
                if (isinstance(o, rdflib.term.URIRef) and 
                    not str(o).startswith(DMLEX + "Has")):
                    subclasses.append(o)
                elif isinstance(o, rdflib.term.BNode):
                    for o2 in g.objects(o, OWL.onProperty):
                        for o3 in g.objects(o, OWL.cardinality):
                            restrictions[class_uri][o2] = f" REQUIRED (exactly {o3})"
                        for o3 in g.objects(o, OWL.maxCardinality):
                            restrictions[class_uri][o2] = f" OPTIONAL (at most {o3})"
                        for o3 in g.objects(o, OWL.minCardinality):
                            restrictions[class_uri][o2] = f" REQUIRED (at least {o3})"

            with open(f"elements/{name}.xml", "w") as f:
                f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE section PUBLIC "-//OASIS//DTD DocBook XML V4.5//EN"
                         "http://www.docbook.org/xml/4.5/docbookx.dtd" [
                         <!ENTITY % xinclude SYSTEM "../../../docbook/xinclude.mod" >
                         %xinclude;
                         <!ENTITY % local.common.attrib "xml:base CDATA #IMPLIED" > 
                         ]>
<section id="rdf_{name}">
    <title>RDF element: <literal>dmlex:{name}</literal></title>

    <para>{definition}</para>
""")
                if subclasses:
                    f.write("""
    <itemizedlist>
        <title>Superclasses</title>""")
                    for s in subclasses:
                        f.write(f"""
        <listitem>
            <para><literal>{s}</literal></para>
        </listitem>""")
                    f.write("""
    </itemizedlist>""")
                f.write("""

    <itemizedlist>
        <title>Properties</title>""")

                for p in props[class_uri]:
                    describe_property(g, p, f, restrictions[class_uri])
                f.write("""
    </itemizedlist>


</section>""")

if __name__ == "__main__":
    parse_rdf()
