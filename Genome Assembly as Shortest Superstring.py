# 问题的难点是怎么知道共同的字符串并且接上去

# 首先要把所有序列提取出来
seq_list = []
stseq = ''
for line in open('long'):
    if line[0] == '>':
        if stseq != '':
            # 把 stseq 添加到 seq_list里
            seq_list.append(stseq)
            stseq = ''
        else:
            continue
    else:
        # 生成stseq
        stseq = stseq + line.strip('\n')
# 这一段的代码的核心是在这最后一行
seq_list.append(stseq)


def MergeMaxOverlap(str_list):
    max_length = -1

    for prefix_index in range(len(str_list)):
        # 不与自己匹配
        list_1 = [num for num in range(len(str_list)) if num != prefix_index]
        for suffix_index in list_1:
            prefix, suffix = str_list[prefix_index], str_list[suffix_index]
            i = 0
            # 如果没有找到相似序列，指针继续+1
            while prefix[i:] != suffix[0:len(prefix[i:])]:
                i += 1
            # 只要匹配大于-1，就改变max_length
            # 用 len长度 实际上得到的数字是从1开始得到的数字
            if len(prefix) - i > max_length:
                max_length = len(prefix) - i
                max_indicies = [prefix_index, suffix_index]


    return [str_list[j] for j in range(len(str_list)) if j not in max_indicies] + \
           [str_list[max_indicies[0]] + str_list[max_indicies[1]][max_length:]]


def LongestCommonSuperstring(str_list):
    while len(str_list) > 1:
        str_list = MergeMaxOverlap(str_list)

    return str_list[0]


if __name__ == '__main__':
    dna_list = [i for i in seq_list]
    super_string = LongestCommonSuperstring(dna_list)

    print (super_string)

