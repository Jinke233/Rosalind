Dict = {}
with open("G:/Rosalind/rosalind_ini6.txt") as f:
    f = f.read().split(" ")
    list = []
    for i in f:
        i= i.strip()
        list.append(i)
    for i in list:
        Dict[i] = list.count(i)
    for x in Dict:
        print (x,Dict[x])
