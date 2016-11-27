
with open('kek.43319559636b94db1c945834340b65d68f90b6ecbb70925f7b24f6efc5c2524e.txt', 'r') as readin:
    for line in readin:
        output = line.split()

print(output)
morse = ''
flag = 1
for each in output:
    if each[0] == 'K' and each[1] == 'E' and each[2] == 'K':
        if flag == 0:
            morse = morse + ('.' * (len(each) - 3))
        else:
            morse = morse + ('-' * (len(each) - 3))
    if each[0] == 'T' and each[1] == 'O' and each[2] == 'P':
        morse = morse + ' '
        flag = (flag + 1)%2
fp = open('morsecode.txt', 'w')
fp.write(morse)
fp.close()
