with open("G:/Rosalind/rosalind_ini2.txt") as f:
    file = f.read().split()
    square = int(float(file[0])**2 + float(file[1])**2)
print(square)
