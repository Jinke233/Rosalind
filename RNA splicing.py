# RNA剪切
# 只需要把所有的字符串都集合成列表形式，同时匹配下面的列表跟第一条列表，匹配到的直接删除
# replace 函数用法

codonTable = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'', 'TAG':'',
'TGC':'C', 'TGT':'C', 'TGA':'', 'TGG':'W',
}

# 首先读取文件，并且储存在一个列表里面



seq_ls = []
seq = ""
with open("rosalind_splc.txt") as infile:
    for line in infile:
        line = line.strip()
        # 思路是下一行的>，添加上一行的序列
        if line.startswith(">"):
            if seq != "":
                seq_ls.append(seq)
                seq = ""
        else:
            seq = seq + line
    # 所以这个时候就要把最后的seq加上去
    seq_ls.append(seq)

# 所有的序列都已经在同一个列表里了
print(len(seq_ls[0]),len(seq_ls[1]),len(seq_ls[2]))
for element in seq_ls[1:]:
        seq_ls[0] = seq_ls[0].replace(element, "")
print(len(seq_ls[0]))

# 最后把密码子转换为蛋白质
protein = ""
for coden in range(0,len(seq_ls[0]),3):
    if seq_ls[0][coden:coden + 3] in codonTable.keys():
        protein = protein + codonTable[seq_ls[0][coden:coden + 3]]
print(protein)


