import rdflib
from glob import glob
from rdflib.namespace import RDF, RDFS, OWL, XSD, Namespace
from collections import defaultdict
from rdflib.collection import Collection

DMLEX = "http://www.oasis-open.org/to-be-confirmed/dmlex#"

def describe_property(g, property, file, restrictions):
    file.write(f"""
    <listitem>
        <para><literal>dmlex:{property.split("#")[-1]}</literal>""")
    if property in restrictions:
        file.write(f""" {restrictions[property]}""")
    for o in g.objects(property, RDFS.range):
        if isinstance(o, rdflib.term.URIRef):
            if str(o).startswith(DMLEX):
                file.write(f""" reference to <olink targetptr="rdf_{str(o)[len(DMLEX):]}">{str(o)[len(DMLEX):]}</olink>""")
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
            props[o].append(s)
        else:
            for listname in g.objects(o, OWL.unionOf):
                for item in Collection(g, listname):
                    props[item].append(s)
    # Generate for each class
    for class_uri in g.subjects(RDF.type, OWL.Class):
        if isinstance(class_uri, rdflib.term.URIRef):
            uri = str(class_uri)
            name = uri.split("#")[-1]

            definition = "DEFINITION MISSING"
            for o in g.objects(class_uri, RDFS.comment):
                definition = str(o)
                break

            subclasses = []
            restrictions = {}
            for o in g.objects(class_uri, RDFS.subClassOf):
                if isinstance(o, rdflib.term.URIRef):
                    subclasses.append(o)
                elif isinstance(o, rdflib.term.BNode):
                    for o2 in g.objects(o, OWL.onProperty):
                        for o3 in g.objects(o, OWL.cardinality):
                            restrictions[o2] = f" REQUIRED (exactly {o3})"
                        for o3 in g.objects(o, OWL.maxCardinality):
                            restrictions[o2] = f" OPTIONAL (at most {o3})"
                        for o3 in g.objects(o, OWL.minCardinality):
                            restrictions[o2] = f" REQUIRED (at least {o3})"

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
                    f.write(f"""
    <itemizedlist>
        <title>Superclasses</title>""")
                    for s in subclasses:
                        f.write(f"""
        <listitem>
            <para><literal>{s}</literal></para>
        </listitem>""")
                    f.write(f"""
    </itemizedlist>""")
                f.write("""

    <itemizedlist>
        <title>Properties</title>""")

                for p in props[class_uri]:
                    describe_property(g, p, f, restrictions)
                f.write("""
    </itemizedlist>


</section>""")

if __name__ == "__main__":
    parse_rdf()
