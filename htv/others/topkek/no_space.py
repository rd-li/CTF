#!/usr/bin/env python3

with open('kek.43319559636b94db1c945834340b65d68f90b6ecbb70925f7b24f6efc5c2524e.txt', 'r') as readin:
    for line in readin:
        output = line.split()

print(output)
morse = ''
for each in output:
    if each[0:3] == 'KEK':
        morse = morse + ('-' * (len(each) - 3))
    if each[0:3] == 'TOP':
        morse = morse + ('.' * (len(each) - 3))
fp = open('morsecode_no_space.txt', 'w')
fp.write(morse)
fp.close()
