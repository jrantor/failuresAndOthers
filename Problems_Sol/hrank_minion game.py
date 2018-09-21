string = input()

vow = 'AEIOU'

kev = 0
stu = 0
l = len(string)

for i in range(l):
    if string[i] in vow:
        kev += l-i
    else:
        stu +=l-i

if (kev > stu):
    print('Kevin ',kev)
elif (kev < stu):
    print('Stuart', stu)
else:
    print('Draw')
