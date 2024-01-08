## Build all the source files so they can be included in the examples
## To use this delete all files in source/ and then
## copy the basic files from jmccrae/dmlex-converter
## and run this script
## e.g.,
##     rm source/*
##     cp ~/projects/jmccrae/dmlex-converter/dmlex/examples/* source/
##     python build_source.py

from glob import glob

N = 74

for f in glob("source/*.xml"):
    with open(f) as inf:
        with open(f + ".xml", "w") as outf:
            outf.write("<programlisting>\n")
            for line in inf.readlines():
                while len(line) > N:
                    outf.write(line[:N].replace("<", "&lt;").replace(">", "&gt;"))
                    outf.write("\n")
                    line = line[N:]
                outf.write(line.replace("<", "&lt;").replace(">", "&gt;"))
            outf.write("</programlisting>\n")

for f in glob("source/*.rdf"):
    with open(f) as inf:
        with open(f + ".xml", "w") as outf:
            n = 1
            outf.write("<programlisting>\n")
            for line in inf.readlines():
                if "PREFIX" not in line and line.strip() != "":
                    while len(line) > N:
                        outf.write(line[:N].replace("<", "&lt;").replace(">", "&gt;"))
                        outf.write("\n")
                        line = line[N:]
                    outf.write(line.replace("<", "&lt;").replace(">", "&gt;"))
            outf.write("</programlisting>\n")

for f in glob("source/*.json"):
    with open(f) as inf:
        with open(f + ".xml", "w") as outf:
            outf.write("<programlisting>\n")
            for line in inf.readlines():
                while len(line) > N:
                    outf.write(line[:N].replace("<", "&lt;").replace(">", "&gt;"))
                    outf.write("\n")
                    line = line[N:]
                outf.write(line.replace("<", "&lt;").replace(">", "&gt;"))
            outf.write("</programlisting>\n")

