with open("G:\\Rosalind\\rosalind_lexf.txt") as f:
    f = f.read().split()
    ls = []
    ls1 = []
    for alpha in f[0:len(f)-1]:
        ls.append(alpha)
    for alpha1 in ls:
        for alpha2 in ls:
            for alpha3 in ls:
                    ls1.append(alpha1+alpha2+alpha3)
for phrase in ls1:
    print (phrase,end="\n")