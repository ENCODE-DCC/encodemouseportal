import sys, string
import re
from ucscGb.gbData.ordereddict import OrderedDict
from ucscGb.gbData.ra.raFile import RaFile
from ucscGb.gbData import ucscUtils
import collections


rafile = RaFile('../data/cv.ra')
metafile = RaFile('../data/mouse_meta.ra')

cell_id = 1
cells = {}
centers = {"CRG-Guigo-m":7,"CSHL-m":7,"Caltech-m":3,"FSU-m":8,"NHGRI-Elnitski":"REMOVE","PSU-m":4,"Stanford-m":5,"UW-m":1,"Yale-m":5,"LICR-m":2}
points = {}
datatype = 0
control = {"Control_32bp":161,"Control_36bp":161,"Control_50bp":161,"IgG-Yale":165,"IgG-mus":162,"IgG-rab":163,"IgG-rat":164,"Input":161,"std":166}
antibodies = {}
targets = {'H3ac':105,'H3K27ac':106,'H3K27me3':107,'H3K36me3':108,'H3K4me1':109,'H3K4me2':110,'H3K4me3':111,'H3K79me2':112,'H3K79me3':113,'H3K9ac':114,'H3K9me3':115,'BHLHE40':116,'CEBPB':117,'CHD1':118
,'CHD2':119,'CTCF':120,'E2F4':121,'EP300':122,'ETS1':123,'FLI1':124,'FOSL1':125,'GABPA':126,'GATA1':127,'GATA2':128,'HCFC1':129,'JUN':130,'JUND':131,'KAT2A':132,'MAFK':133,'MAX':134,'MAZ':135,'MXI1':136
,'MYB':137,'MYC':138,'MYOD1':139,'MYOG':140,'PAX5':141,'POLR2A':142,'RAD21':143,'RCOR1':144,'RDBP':145,'REST':146,'SIN3A':147,'SMC3':148,'SRF':149,'TAL1':150,'TBP':151,'TCF12':152,'TCF3':153,'UBTF':154
,'USF1':155,'USF2':156,'ZC3H11A':157,'ZKSCAN1':158,'ZMIZ1':159,'ZNF384':160}
cell_item_id = 4001
center_id = 2001
exps = {}
exps2 = {}


for key in rafile.keys():
    thisstanza = rafile[key]

    if thisstanza['type'] == 'Cell Line':
        if thisstanza['organism'] == 'mouse':
            cells[thisstanza['term']] = cell_id
            cell_id +=1

for key in rafile.keys():
    thisstanza = rafile[key]

    if thisstanza['type'] == 'Antibody':
        antibodies[thisstanza['term']] = thisstanza['target']

for data in metafile.keys():
    thisstanza = metafile[data]

    if 'view' not in thisstanza:
        continue

    else:
        
        if thisstanza['expId'] in points.keys():
            continue
        else:

            if thisstanza['dataType'] == 'Bip':
                datatype = 0
            elif thisstanza['dataType'] == 'Mapability':
                datatype = 0
            elif thisstanza['dataType'] == 'DnaseSeq':
                datatype = 101
            elif thisstanza['dataType'] == 'DnaseDgf':
                datatype = 102
            elif thisstanza['dataType'] == 'RnaSeq':
                datatype = 103
            elif thisstanza['dataType'] == 'RepliChip':
                datatype = 104
            elif thisstanza['dataType'] == 'ChipSeq':
                if thisstanza['antibody'] == 'Input':
                    datatype = control[thisstanza['control']]
                else:
                    target = antibodies[thisstanza['antibody']]
                    datatype = targets[target]

            if datatype == 0:
                continue
            else:
                cell = cells[thisstanza['cell']]
                center = centers[thisstanza['lab']]

                exp = cell,datatype
                exp2 = cell,datatype,center
                if exp in exps.keys():
                    if exp2 in exps2.keys():
                        continue
                    else:
                        print "insert into MEPages_celldataitem_centers values (",center_id,",",exps[exp],",",center,");"
                        center_id +=1
                        exps2[exp2]=1
                else:
                    print "insert into MEPages_celldataitem values (",cell_item_id,",",datatype,",",cell,",NULL,NULL,NULL);" 
                    print "insert into MEPages_celldataitem_centers values (",center_id,",",cell_item_id,",",center,");"
                    exps[exp]=cell_item_id
                    exps2[exp2]=1
                    cell_item_id +=1
                    center_id +=1
               
                points[thisstanza['expId']] = 1
                    

            

