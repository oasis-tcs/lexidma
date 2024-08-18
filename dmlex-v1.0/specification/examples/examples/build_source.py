## Build all the source files so they can be included in the examples
from glob import glob

N = 74

for f in glob("source/*.xml"):
    if f.endswith(".xml.xml") or f.endswith(".rdf.xml") or f.endswith(".json.xml"):
        continue
    with open(f) as inf:
        with open(f + ".xml", "w") as outf:
            outf.write("<!-- This example is automatically generated. DO NOT EDIT -->\n")
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
            outf.write("<!-- This example is automatically generated. DO NOT EDIT -->\n")
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
            outf.write("<!-- This example is automatically generated. DO NOT EDIT -->\n")
            outf.write("<programlisting>\n")
            for line in inf.readlines():
                while len(line) > N:
                    outf.write(line[:N].replace("<", "&lt;").replace(">", "&gt;"))
                    outf.write("\n")
                    line = line[N:]
                outf.write(line.replace("<", "&lt;").replace(">", "&gt;"))
            outf.write("</programlisting>\n")

for f in glob("source/*.nvh"):
    with open(f) as inf:
        with open(f + ".xml", "w") as outf:
            outf.write("<!-- This example is automatically generated. DO NOT EDIT -->\n")
            outf.write("<programlisting>\n")
            for line in inf.readlines():
                while len(line) > N:
                    outf.write(line[:N].replace("<", "&lt;").replace(">", "&gt;"))
                    outf.write("\n")
                    line = line[N:]
                outf.write(line.replace("<", "&lt;").replace(">", "&gt;"))
            outf.write("</programlisting>\n")

