seq = {}
with open('rosalind_grph.txt','r') as f:
        for line in f:
                line = line.rstrip()
                if line.startswith('>'):
                        seqname = line[1:]
                        seq[seqname] = ''
                        continue
                seq[seqname] += line.upper()

with open("out_ro_graph.txt", "w") as output_file:
    for key , value in seq.items():
            for key2 ,value2 in seq.items():
                    if key != key2 and value[-3:] == value2[:3]:
                            print(key+'\t'+key2, file = output_file)