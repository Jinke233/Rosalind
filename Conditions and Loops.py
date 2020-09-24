with open("G:/Rosalind/rosalind_ini4.txt") as f:
    f = f.readline().split(" ")
    start = int(f[0])
    end = int(f[1])
    # list = []
    flag = 0
    for number in range(start,end + 1):
        if number %2 == 1:
    #         list.append(number)
    # print(sum(list))
            flag = flag + number
        else:
            continue
    print (flag)

