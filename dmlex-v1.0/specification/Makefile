html: dmlex-v1.0-wd01.html

pdf: dmlex-v1.0-wd01.pdf

dmlex-v1.0-wd01.pdf: dmlex-v1.0-wd01.fo
	fop -pdf $@ -fo $<

dmlex-v1.0-wd01.fo: dmlex-v1.0-wd01.xml
	xsltproc --xinclude -o $@ stylesheets/oasis-specification-fo-a4.xsl $<

dmlex-v1.0-wd01.html: dmlex-v1.0-wd01.xml
	xsltproc --xinclude -o $@ stylesheets/oasis-specification-html.xsl $<

dmlex-v1.0-wd01.xml: dmlex.xml $(shell xmlstarlet sel -T -t -m //xi:include/@href -v . -n dmlex.xml)
	./merge.sh
