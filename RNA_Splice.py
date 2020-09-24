# 这个脚本是为了从序列去除内含子只获取外显子并且连接在一起，并且翻译成蛋白质
#解题思路首先把它们全部都变为列表，之后碰撞即可
#不理解代码的意思
Seq_list = list()
Stseq = ""
with open(r"G:\Rosalind\rosalind_splc.txt") as file:
    for line in file:
        line = line.strip()
        if ">" in line:
            if Stseq != '':
                Seq_list.append(Stseq)
                Stseq = ''
            
        else:
            Stseq = Stseq + line
print(Seq_list)
