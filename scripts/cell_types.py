import sys, string
import re
from ucscGb.gbData.ordereddict import OrderedDict
from ucscGb.gbData.ra.raFile import RaFile
from ucscGb.gbData import ucscUtils
import collections


rafile = RaFile('../data/cv.ra')

cell_id = 1
for key in rafile.keys():
    thisstanza = rafile[key]

    if thisstanza['type'] == 'Cell Line':
        if thisstanza['organism'] == 'mouse':
            if 'label' not in thisstanza:
                thisstanza['label'] = thisstanza['term']

            if 'color' not in thisstanza:
                thisstanza['color'] ='5'
            if thisstanza['color'] == '102,50,200':
                thisstanza['color'] = '1'
            elif thisstanza['color'] == '139,69,19':
                thisstanza['color'] = '2'
            elif thisstanza['color'] == '153,38,0':
                thisstanza['color'] = '3'
            elif thisstanza['color'] == '105,105,105':
                thisstanza['color'] = '4'
            elif thisstanza['color'] == '230,159,0':
                thisstanza['color'] = '6'
            elif thisstanza['color'] == '204,121,167':
                thisstanza['color'] = '7'
            elif thisstanza['color'] == '189,0,157':
                thisstanza['color'] = '8'
            elif thisstanza['color'] == '0,158,115':
                thisstanza['color'] = '9'
            elif thisstanza['color'] == '86,180,233':
                thisstanza['color'] = '10'
            elif thisstanza['color'] == '65,105,225':
                thisstanza['color'] = '11'

            print "insert into MEPages_celltissuetype value (",cell_id,",'",thisstanza['label'],"','",thisstanza['label'],"','",thisstanza['term'],"',",0,",","NULL",",'",thisstanza['color'],"',",2,")"
            cell_id +=1
