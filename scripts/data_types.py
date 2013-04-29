import sys, string
import re
from ucscGb.gbData.ordereddict import OrderedDict
from ucscGb.gbData.ra.raFile import RaFile
from ucscGb.gbData import ucscUtils
import collections


rafile = RaFile('../data/mouse_meta.ra')
cvfile = RaFile('../data/cv.ra')

for key in rafile.keys():
    thisstanza = rafile[key]
    
    if 'antibody' not in thisstanza:
        continue

    else:
        print thisstanza["antibody"]
