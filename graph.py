## overlap ##
from collections import OrderedDict
import re

def overlap_graph(dna,n):
    edges = []
    for ke1, val1 in dna:
        for ke2, val2 in dna:     #定义函数调用要注意名称
            if ke1 != ke2 and val1[-n:] == val2[0:n]:
               edges.append(ke1+'\t'+ke2)
    return edges

seq = OrderedDict()

with open ('rosalind_grph.txt') as f:
     for line in f:
         line = line.rstrip()
         if line.startswith('>'):
            seqName = re.sub('>','',line)
            seq[seqName] = ''
            continue
         seq[seqName] += line.upper()  #注意if的用法

dna =seq.items()

fh = open('rosalind_grph_output.txt', 'wt')

for x in overlap_graph(dna,3):
    fh.write(x+'\n')

fh.close()