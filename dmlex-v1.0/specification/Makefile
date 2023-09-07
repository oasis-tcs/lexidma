include Makefile.dep

html: dmlex-v1.0-wd01.html

pdf: dmlex-v1.0-wd01.pdf

dmlex-v1.0-wd01.pdf: dmlex-v1.0-wd01.fo
	fop -c stylesheets/fop.xconf -pdf $@ -fo $<

dmlex-v1.0-wd01.fo: dmlex-v1.0-wd01.xml
	xsltproc --xinclude -o $@ stylesheets/oasis-specification-fo-a4.xsl $<

dmlex-v1.0-wd01.html: dmlex-v1.0-wd01.xml
	xsltproc --xinclude -o $@ stylesheets/oasis-specification-html.xsl $<

dmlex-v1.0-wd01.xml: dmlex.xml docbook/dbgenent.mod $(SOURCE_XML)
	./merge.sh

Makefile.dep: dmlex.xml $(SOURCE_XML) makedep.sh
	echo -n "SOURCE_XML=" > $@
	./makedep.sh >> $@
