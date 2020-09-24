# Finding a Shared Motif

def readfasta(filename, sample):
    fa = open(filename, 'r')
    fo = open(sample, 'w')
    res = {}
    rres = []
    ID = ''
    for line in fa:
        # 如果是">"开头的，就创建一个key键
        if line.startswith('>'):
            ID = line.strip('\n')
            res[ID] = ''
        # 如果不是">"开头的，在这个key键下添加value值
        else:
            res[ID] += line.strip('\n')
    # 把value值提取出，写入sample文件
    for value in res.values():
        rres.append(value)
        fo.write(value + '\n')
    #返回 ['TAGACCA','ATACA','GATTACA']
    return rres


def fragement(seq_list):
    res = []
    seq = seq_list[0]       # TAGACCA
    for i in range(len(seq)):
        s_seq = seq[i:]
        for j in range(len(s_seq)):
            res.append(s_seq[:(len(s_seq) - j)])
    # 返回res列表的所有组合
    # T TA TAG TAGA TAGAC TAGACC TAGACCA
    # A AG AGA
    return res


def main(infile, sample):
    seq_list = readfasta(infile, sample)
    frags = fragement(seq_list)
    frags.sort(key=len, reverse=True)  # 从长到短排列
    for i in range(len(frags)):
        ans = []
        for j in seq_list:
            # 把"所有组合"匹配到"列表"里面，有些匹配1次，有些匹配2次，
            # 匹配三次的就是share_motif
            r = j.count(frags[i])
            if r != 0:
                ans.append(r)
        # 判断匹配是否大于等于三次
        if len(ans) >= len(seq_list):
            # 打印匹配大于等于三次的
            print(frags[i])
            # break


main('./Finding a Shared Motif', 'sample.txt')
