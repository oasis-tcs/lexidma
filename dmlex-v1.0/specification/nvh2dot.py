#!/usr/bin/python

import sys
import os
from collections import defaultdict
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(SCRIPT_DIR + "/lib")
from nvh import nvh
dmlex = nvh.parse_file(sys.stdin)
object_names = {c.name for c in dmlex.children}
object_labels = {
    "core": ("Core", "black"),
    "annotation": ("Annotation Module", "yellow"),
    "etymology": ("Etymology Module", "green"),
    "linking": ("Linking Module", "blue"),
    "values": ("Controlled Values Module", "orange"),
    "xlingual": ("Crosslingual Module", "pink")
}
def quant2uml (s):
    import re
    if not s or s.startswith("("):
        return "1..1%s" % s
    s = re.sub(r"^\([0-9]\)+\+", "\1..*", s)
    s = re.sub(r"^\?", "0..1", s)
    s = re.sub(r"^\+", "1..*", s)
    s = re.sub(r"^\*", "0..*", s)
    return s

object_types = defaultdict(dict)
edges = []
edge_order = ["core", "values", "linking", "xlingual", "etymology", "xlingual", "annotation"]
for n in object_names:
    module, name = n.split("@")
    object_types[module][name] = []
for obj in dmlex.children:
    obj_module, obj_name = obj.name.split("@")
    for prop in obj.children:
        if prop.name in object_names:
            if prop.value:
                headlabel=",xlabel=<%s>" % quant2uml(prop.value)
            else:
                headlabel=""
            edges.append('"%s"->"%s"[arrowhead=odiamond%s];' % (prop.name, obj.name, headlabel))
        else:
            object_types[obj_module][obj_name].append (prop.name + ": " + quant2uml(prop.value))
edges.sort(key=lambda e: edge_order.index(e.split("@")[0].strip('"')))
for e in edges:
    print(e)
for m in object_types:
    print('subgraph cluster_%s {\nrank="same"; label=<<B>%s</B>>; color=%s;' % (m, object_labels[m][0].upper(), object_labels[m][1]))
    for obj in object_types[m]:
        label = "<B>%s</B><BR/>" % obj 
        label += "<BR/>".join(object_types[m][obj])
        print('"%s@%s"[label=<%s>];' % (m,obj,label))
    print('}')
