-include Makefile.dep

VERSION=v1.0-os

html: dmlex-$(VERSION).html

pdf: dmlex-$(VERSION).pdf

dmlex-$(VERSION).pdf: dmlex-$(VERSION).fo
	fop -c stylesheets/fop.xconf -pdf $@ -fo $<

dmlex-$(VERSION).fo: dmlex-$(VERSION).xml
	xsltproc --xinclude -o $@ stylesheets/oasis-specification-fo-a4.xsl $<

dmlex-$(VERSION).html: dmlex-$(VERSION).xml
	xsltproc --xinclude -o $@ stylesheets/oasis-specification-html.xsl $<

dmlex-$(VERSION).xml: dmlex.xml docbook/dbgenent.mod dmlex_uml.svg $(SOURCE_XML)
	./merge.sh $@
	xmllint --valid --noout $@

dmlex_uml.pdf: dmlex.dot
	dot -Tpdf < $< > $@

dmlex_uml.svg: dmlex.dot
	dot -Tsvg < $< > $@

dmlex.dot: dmlex.dot.m4 dmlex.dot.content
	m4 $< > $@

dmlex.dot.content: schemas/informativeCopiesOf3rdPartySchemas/NVH/dmlex_model_description.nvh nvh2dot.py
	awk '/<programlisting>/,/<\/programlisting>/' $< | tail -n+2 | head -n-1 | ./nvh2dot.py > $@

Makefile.dep: dmlex.xml $(SOURCE_XML) makedep.sh
	echo -n "SOURCE_XML=" > $@
	./makedep.sh >> $@

.PHONY: clean validate_xml validate_json validate_rdf
clean:
	rm -f dmlex-$(VERSION).html dmlex-$(VERSION).pdf dmlex-$(VERSION).fo dmlex-$(VERSION).xml Makefile.dep dmlex_uml.svg dmlex_uml.pdf dmlex.dot dmlex.dot.content

xmldep:
	@python -c 'import xmlschema' 2>/dev/null || { echo "Python xmlschema module is not installed, cannot validate XML examples."; exit 2; }

jsondep:
	@python -c 'import jsonschema' 2>/dev/null || { echo "Python jsonschema module is not installed, cannot validate JSON examples."; exit 2; }

rdfdep:
	@python -c 'import pyshacl' 2>/dev/null || { echo "Python pyshacl module is not installed, cannot validate JSON examples."; exit 2; }

validate_xml: xmldep validate_xml.py schemas/XML/dmlex.xsd schemas/XML/dmlex_no-crosslingual.xsd
	@for xmlexample in examples/examples/source/*[0-9].xml; do \
		echo validating "$$xmlexample"; \
		./validate_xml.py schemas/XML/dmlex.xsd < "$$xmlexample" 2>/dev/null \
		|| \
		./validate_xml.py schemas/XML/dmlex_no-crosslingual.xsd < "$$xmlexample" 2>/dev/null \
		|| { echo "validation of $$xmlexample failed -- none of the following validations succeeded:"; \
		     echo ./validate_xml.py schemas/XML/dmlex.xsd "< $$xmlexample"; \
			 echo ./validate_xml.py schemas/XML/dmlex_no-crosslingual.xsd "< $$xmlexample" ; \
			 exit 3; \
		   } \
	done

validate_json: jsondep validate_json.py schemas/JSON/dmlex.schema.json schemas/JSON/dmlex_no-crosslingual.schema.json
	@for jsonexample in examples/examples/source/*[0-9].json; do \
		echo validating "$$jsonexample"; \
		./validate_json.py schemas/JSON/dmlex.schema.json < "$$jsonexample" 2>/dev/null \
		|| \
		./validate_json.py schemas/JSON/dmlex_no-crosslingual.schema.json < "$$jsonexample" 2>/dev/null \
		|| { echo "validation of $$jsonexample failed -- none of the following validations succeeded:"; \
		     echo ./validate_json.py schemas/JSON/dmlex.schema.json "< $$jsonexample"; \
			 echo ./validate_json.py schemas/JSON/dmlex_no-crosslingual.schema.json "< $$jsonexample" ; \
			 exit 4; \
		   } \
	done

validate_rdf: rdfdep schemas/RDF/dmlex.shacl
	@for rdfexample in examples/examples/source/*[0-9].rdf; do \
		echo validating "$$rdfexample"; \
		python -m pyshacl -s schemas/RDF/dmlex.shacl -df turtle $$rdfexample -e schemas/RDF/dmlex.ttl -i rdfs \
		|| { echo "validation of $$rdfexample failed"; \
			 exit 5; \
		   } \
	done
