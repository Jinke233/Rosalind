Write_file = open("G:/Rosalind/rosalind_ini5_write.txt","w")
with open("G:/Rosalind/rosalind_ini5.txt") as f:
    f = f.readlines()
    num_line = len(f) + 1
    if num_line % 2 == 0:
        num_line = len(f)
    else:
        num_line = len(f)
    for number in range(0,num_line ):
        if number % 2 != 0:
            Write_file.write(f[number].strip() + "\n")