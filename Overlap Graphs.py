# 重叠图
# 要求把具有收尾三个字符串相同的序列的head提取构成邻接矩阵

# 思路 单个迭代



aDict={}
with open("grph.txt", "w") as output_file:
    for line in open("rosalind_grph.txt"):
       if  line[0]=='>' :
         key  =line.strip()
         aDict[key]=[]
       else:
         aDict[key].append(line.strip())
    for key,valueL in aDict .items():
      print(key + "\n" + ''.join(valueL), file = output_file)

head_list = list()
seq_list = list()
line = ""
# 首先读取文件 分别存储两个文件
with open("grph.txt" ) as infile:
    for line in infile:
        line = line.strip()
        if line.startswith(">") :
            head_list.append(line)
        else:
            seq_list.append(line)

# 对seq_list 进行迭代， 如果满足条件直接索引head_list位置
# 第一层迭代
with open("out_grph.txt","w") as out_file:
    for number in range(len(seq_list)):
        head = seq_list[number][-3:]
        # 第二层迭代
        # 这里我出现一个误区就是我以为只能在自己后面接序列，实际上可以，还是题目没有吃透
        for seq in seq_list:
            if head == seq[:3]:
                head_name = head_list[number]
                tail_name = head_list[seq_list.index(seq)]
                if head_name != tail_name:
                    print(head_name[1:] + " " + tail_name[1:], file = out_file)

