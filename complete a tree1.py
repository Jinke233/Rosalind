f = open('rosalind_tree.txt', 'r')
lines = f.readlines()
f.close()

num = lines[0] # 存储结点的数目
edges = lines[1:] # 存储边的关系
i = 1
nodes = []
while i <= int(num):
    nodes.append(str(i)) # 用一个列表保存所有节点
    i += 1

fedge = edges[0].replace('\n','') # 把邻接表第一行取出来，作为第一“堆”的基础
fedge = fedge.split(' ')
nodes.remove(fedge[0])
nodes.remove(fedge[1])
tree = [fedge] # tree用来存储结点通过邻接表存储的关系形成的“堆”
flag = 1 # flag存储现在tree里有几“堆”
i = 1
while i < len(edges): # i遍历邻接表
    edge = edges[i].replace('\n','')
    edge = edge.split(' ')
    if edge[0] in nodes:
        nodes.remove(edge[0]) # 每取出一个边，就把形成边的结点从结点列表中删去
        if edge[1] in nodes:
            nodes.remove(edge[1])
        j = 0
        tag = 0
        note = []
        while j < flag: # j用来遍历各“堆”
            if edge[0] in tree[j]: # 如果这条边的一个结点已经在其中一个“堆”里
                tree[j].append(edge[1]) # 把这个边加入这一“堆”
                tag += 1
                note.append(j) # note存储这个结点在哪个“堆”
                j += 1
            elif edge[1] in tree[j]:
                tree[j].append(edge[0])
                tag += 1
                note.append(j)
                j += 1
            else: # 如果不在这一“堆”里，j加一，以查找下一“堆”
                j += 1
        if tag == 0: # 如果在之前存在的“堆”里都没有这条边
            tree.append(edge)
            flag += 1 # 添加一个新的“堆”
        if tag == 2: # 如果两个结点各在两“堆”中，说明这两个“堆”可以合并
            flag -= 1
            tree[note[0]].extend(tree[note[1]])
            tree.remove(tree[note[1]]) # 合并两“堆”并删去其中一个
            tree[note[0]].remove(edge[0])
            tree[note[0]].remove(edge[1]) # 删去由合并导致的重复结点

        i += 1

        print(tree)
        lennodes = len(nodes) # 记录现在结点列表中还有几个结点，每个都相当于一个单独的“堆”
        sum = (flag - 1) + lennodes # “堆”的数量减去一即为需要添加的边的数量
        print(sum)

