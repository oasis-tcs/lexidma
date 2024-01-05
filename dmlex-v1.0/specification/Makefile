include Makefile.dep

html: dmlex-v1.0-csd02.html

pdf: dmlex-v1.0-csd02.pdf

dmlex-v1.0-csd02.pdf: dmlex-v1.0-csd02.fo
	fop -c stylesheets/fop.xconf -pdf $@ -fo $<

dmlex-v1.0-csd02.fo: dmlex-v1.0-csd02.xml
	xsltproc --xinclude -o $@ stylesheets/oasis-specification-fo-a4.xsl $<

dmlex-v1.0-csd02.html: dmlex-v1.0-csd02.xml
	xsltproc --xinclude -o $@ stylesheets/oasis-specification-html.xsl $<

dmlex-v1.0-csd02.xml: dmlex.xml docbook/dbgenent.mod dmlex_uml.svg $(SOURCE_XML)
	./merge.sh

dmlex_uml.pdf: dmlex.dot
	dot -Tpdf < $< > $@

dmlex_uml.svg: dmlex.dot
	dot -Tsvg < $< > $@

dmlex.dot: dmlex.dot.m4 dmlex.dot.content
	m4 $< > $@

dmlex.dot.content: dmlex.nvh nvh2dot.py
	awk '/<programlisting>/,/<\/programlisting>/' $< | tail -n+2 | head -n-1 | ./nvh2dot.py > $@

Makefile.dep: dmlex.xml $(SOURCE_XML) makedep.sh
	echo -n "SOURCE_XML=" > $@
	./makedep.sh >> $@

clean:
	rm dmlex-v1.0-csd02.html dmlex-v1.0-csd02.pdf dmlex-v1.0-csd02.fo dmlex-v1.0-csd02.xml Makefile.dep dmlex_uml.svg dmlex_uml.pdf dmlex.dot dmlex.dot.content
