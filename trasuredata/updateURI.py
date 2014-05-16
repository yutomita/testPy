# -*- coding: utf-8 -*-
import csv
import re
from struct import *


with open("url_title_master.tsv", "rb") as f:
    tsv = csv.reader(f, delimiter='\t')

    arr = []
    i = 0
    for line in tsv:
        i += 1
#        print i
        prog = re.compile("^[httpsfile]+:\/{2,3}([0-9a-z\.\-:]+?):?[0-9]*?\/")
        subDomain = prog.search(line[1])
        if subDomain:
            if subDomain.group() == line[1]:
                tes = []
                tes.append(subDomain.group(1))
                tes.append(line[2])
                arr.append(tes)
                #arr.append(subDomain.group(1) + "\t" + str(line[2]))
                #print subDomain.group(1) + "\t" + line[1] + "\t" + line[2]
                #i += 1
        else:
            #print "NO!!:%s" % line[1]
            #arr.append(line[1] + "\t" + line[2])
            tes = []
            tes.append(line[1])
            tes.append(line[2])
            arr.append(tes)

#        if i > 13:
#            break

#    print i
    with open("sub_domain_title_master2.tsv", "wb") as f2:
        writer = csv.writer(f2, delimiter="\t")
        writer.writerows(arr)




