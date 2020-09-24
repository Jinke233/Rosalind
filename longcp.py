# 这是非常常用的提取fasta序列的代码
seq_list = []
stseq = ""
for line in open("long"):
    line = line.strip()
    if line[0] == ">":
        if stseq != "":
            seq_list.append(stseq)
            stseq = ""
        else:
            continue
    else;
    # 生成stseq
        stseq = stseq + line
seq_list.append(stseq)


