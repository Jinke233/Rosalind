# coding=utf-8
'''
A solution to a ROSALIND bioinformatics problem.
Problem Title: Finding a Shared Motif
Rosalind ID: LCSM
Rosalind #: 014
URL: [url]http://rosalind.info/problems/lcsm/[/url]
'''


def LongestSubstring(string_list):
    '''Extracts all substrings from the first string in a list, and sends longest substring candidates to be checked.'''
    longest = ''
    for start_index in range(len(string_list[0])):
        for end_index in range(len(string_list[0]), start_index, -1):
            # Break if the length becomes too small, as it will only get smaller.
            if end_index - start_index <= len(longest):
                break
            elif CheckSubstring(string_list[0][start_index:end_index], string_list):
                longest = string_list[0][start_index:end_index]

    return longest


def CheckSubstring(find_string, string_list):
    'Checks if a given substring appears in all members of a given collection of strings and returns True/False.'
    for string in string_list:
        if (len(string) < len(find_string)) or (find_string not in string):
            return False
    return True


seq = {}
seq_name = ''
with open('14.txt') as f:
    for line in f:
        if line[0] == '>':
            seq_name = line.rstrip()
            seq[seq_name] = ''
            continue
        else:
            seq[seq_name] += (line.rstrip()).upper()

print(seq)

if __name__ == '__main__':
    dna = []
    for seq_name in seq:
        dna.append(seq[seq_name])

    lcsm = LongestSubstring(dna)
    print(lcsm)
    with open('014_LCSM.txt', 'w') as output_data:
        output_data.write(lcsm)
