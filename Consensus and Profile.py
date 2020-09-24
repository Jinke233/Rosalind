# Consensus and Profile

#这个类是用来在原来的数据类型的基础上进行优化的
from collections import  *



fh = open("Consensus and Profile_output.txt", "w")

# 建立一个新的排序的字典
rosalind = OrderedDict()
seqLength = 0
with open("Rosalind_cons.txt") as f:
    for line in f:
        line = line.rstrip()
        if line.startswith(">"):
            rosalindName = line
            rosalind[rosalindName] = ""
            continue
        # 这里很具有借鉴意义，因为完全省去一大堆 elif的麻烦
        rosalind[rosalindName] += line
    seqLength = len(rosalind[rosalindName])


A,C,G,T = [],[],[],[]
consensusSeq = ""
for i in range(seqLength):
    seq = ""
    for k in rosalind.keys():
        seq += rosalind[k][i]
    A.append(seq.count('A'))
    C.append(seq.count('C'))
    G.append(seq.count('G'))
    T.append(seq.count('T'))
    counts = Counter(seq)
    consensusSeq += counts.most_common()[0][0]   # most_common()数据结构发生变化，直接变为列表

fh.write(consensusSeq + '\n')
# map 函数 也用的特别好，直接就是把数字改成str格式，而且更加优雅
fh.write('\n'.join(['A:\t' + '\t'.join(map(str, A)), 'C:\t' + '\t'.join(map(str, C)),
                    'G:\t' + '\t'.join(map(str, G)), 'T:\t' + '\t'.join(map(str, T))]))

fh.close()