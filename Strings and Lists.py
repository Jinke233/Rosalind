with open("G:/Rosalind/rosalind_ini3.txt") as f:
    f = f.readlines()
    list=f[1].split(" ")
    Indices = []
    for number in list:
        number = int(number)
        Indices.append(number)
one_word = f[0][Indices[0]:Indices[1]+1]
two_word = f[0][Indices[2]:Indices[3]+1]
print (one_word,two_word)